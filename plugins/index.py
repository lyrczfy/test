import logging
import asyncio
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import ChannelInvalid, ChatAdminRequired, UsernameInvalid, UsernameNotModified
from info import ADMINS
from info import INDEX_REQ_CHANNEL as LOG_CHANNEL
from database.ia_filterdb import save_file
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils import temp
import re
import time
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
lock = asyncio.Lock()

# Configuration for rate limiting and batching
BATCH_SIZE = 200  # Process messages in batches (can be increased for efficiency)
RATE_LIMIT = 0.5  # Seconds between batches to avoid FloodWait

# For tracking progress
class IndexStats:
    def __init__(self):
        self.total_files = 0
        self.duplicate = 0
        self.errors = 0
        self.deleted = 0
        self.no_media = 0
        self.unsupported = 0
        self.processed = 0
        self.start_time = None
        self.is_cancelled = False
    
    def start(self):
        self.start_time = datetime.now()
    
    def get_elapsed_time(self):
        if not self.start_time:
            return "0s"
        elapsed = datetime.now() - self.start_time
        seconds = elapsed.total_seconds()
        if seconds < 60:
            return f"{seconds:.1f}s"
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{int(minutes)}m {int(seconds)}s"
    
    def get_speed(self):
        if not self.start_time:
            return "0 msg/s"
        elapsed = (datetime.now() - self.start_time).total_seconds()
        if elapsed <= 0:
            return "0 msg/s"
        return f"{self.processed/elapsed:.2f} msg/s"
    
    def format_stats(self):
        return (f"Progress: <code>{self.processed}</code> messages\n"
                f"Saved: <code>{self.total_files}</code> files\n"
                f"Duplicates: <code>{self.duplicate}</code>\n"
                f"Deleted msgs: <code>{self.deleted}</code>\n"
                f"Non-media: <code>{self.no_media}</code>\n"
                f"Unsupported: <code>{self.unsupported}</code>\n"
                f"Errors: <code>{self.errors}</code>\n"
                f"Speed: <code>{self.get_speed()}</code>\n"
                f"Elapsed: <code>{self.get_elapsed_time()}</code>")


@Client.on_callback_query(filters.regex(r'^index'))
async def index_files(bot, query):
    if query.data.startswith('index_cancel'):
        temp.CANCEL = True
        return await query.answer("Cancelling Indexing")
    
    _, raju, chat, lst_msg_id, from_user = query.data.split("#")
    
    if raju == 'reject':
        await query.message.delete()
        await bot.send_message(int(from_user),
                               f'Your Submission for indexing {chat} has been declined by our moderators.',
                               reply_to_message_id=int(lst_msg_id))
        return

    if lock.locked():
        return await query.answer('Wait until previous process complete.', show_alert=True)
    
    msg = query.message

    await query.answer('Processing...⏳', show_alert=True)
    if int(from_user) not in ADMINS:
        await bot.send_message(int(from_user),
                               f'Your Submission for indexing {chat} has been accepted by our moderators and will be added soon.',
                               reply_to_message_id=int(lst_msg_id))
    
    await msg.edit(
        "Starting Indexing",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton('Cancel', callback_data='index_cancel')]]
        )
    )
    
    try:
        chat = int(chat)
    except:
        chat = chat
        
    await batch_index_files(int(lst_msg_id), chat, msg, bot)


@Client.on_message((filters.forwarded | (filters.regex("(https://)?(t\.me/|telegram\.me/|telegram\.dog/)(c/)?(\d+|[a-zA-Z_0-9]+)/(\d+)$")) & filters.text ) & filters.private & filters.incoming & filters.user(ADMINS))
async def send_for_index(bot, message):
    if message.text:
        regex = re.compile("(https://)?(t\.me/|telegram\.me/|telegram\.dog/)(c/)?(\d+|[a-zA-Z_0-9]+)/(\d+)$")
        match = regex.match(message.text)
        if not match:
            return await message.reply('Invalid link')
        chat_id = match.group(4)
        last_msg_id = int(match.group(5))
        if chat_id.isnumeric():
            chat_id  = int(("-100" + chat_id))
    elif message.forward_from_chat.type == enums.ChatType.CHANNEL:
        last_msg_id = message.forward_from_message_id
        chat_id = message.forward_from_chat.username or message.forward_from_chat.id
    else:
        return
        
    try:
        await bot.get_chat(chat_id)
    except ChannelInvalid:
        return await message.reply('This may be a private channel / group. Make me an admin over there to index the files.')
    except (UsernameInvalid, UsernameNotModified):
        return await message.reply('Invalid Link specified.')
    except Exception as e:
        logger.exception(e)
        return await message.reply(f'Errors - {e}')
        
    try:
        k = await bot.get_messages(chat_id, last_msg_id)
    except:
        return await message.reply('Make Sure That I am An Admin In The Channel, if channel is private')
    if k.empty:
        return await message.reply('This may be group and I am not an admin of the group.')

    buttons = [
        [
            InlineKeyboardButton('Yes',
                                callback_data=f'index#accept#{chat_id}#{last_msg_id}#{message.from_user.id}')
        ],
        [
            InlineKeyboardButton('close', callback_data='close_data'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    return await message.reply(
        f'Do you Want To Index This Channel/ Group ?\n\nChat ID/ Username: <code>{chat_id}</code>\nLast Message ID: <code>{last_msg_id}</code>',
        reply_markup=reply_markup)


@Client.on_message((filters.forwarded | (filters.regex("(https://)?(t\.me/|telegram\.me/|telegram\.dog/)(c/)?(\d+|[a-zA-Z_0-9]+)/(\d+)$")) & filters.text ) & filters.private & filters.incoming & ~filters.user(ADMINS))
async def deny_for_non_admins(bot, message):
    await message.reply("Sorry, only administrators can use the index functionality.")


@Client.on_message(filters.command('setskip') & filters.user(ADMINS))
async def set_skip_number(bot, message):
    if ' ' in message.text:
        _, skip = message.text.split(" ")
        try:
            skip = int(skip)
        except:
            return await message.reply("Skip number should be an integer.")
        await message.reply(f"Successfully set SKIP number as {skip}")
        temp.CURRENT = int(skip)
    else:
        await message.reply("Give me a skip number")


async def process_message(message, stats):
    """Process a single message and update statistics"""
    if message.empty:
        stats.deleted += 1
        return False

    if not message.media:
        stats.no_media += 1
        return False
        
    if message.media not in [enums.MessageMediaType.VIDEO, enums.MessageMediaType.AUDIO, enums.MessageMediaType.DOCUMENT]:
        stats.unsupported += 1
        return False
        
    media = getattr(message, message.media.value, None)
    if not media:
        stats.unsupported += 1
        return False
        
    media.file_type = message.media.value
    media.caption = message.caption
    
    try:
        aynav, vnay = await save_file(media)
        if aynav:
            stats.total_files += 1
        elif vnay == 0:
            stats.duplicate += 1
        elif vnay == 2:
            stats.errors += 1
        return True
    except Exception as e:
        logger.error(f"Error processing message {message.id}: {e}")
        stats.errors += 1
        return False


async def process_single_batch(bot, chat, message_ids, stats):
    """Process a single batch of messages in strict order"""
    try:
        # Get messages in batch (this preserves order by message_id)
        messages = await bot.get_messages(chat, message_ids)
        
        # Process each message in strict order
        for i, message in enumerate(messages):
            if stats.is_cancelled:
                return
            
            # Process the message
            await process_message(message, stats)
            stats.processed += 1
            
            # Add a tiny pause every 20 messages to reduce FloodWait risk
            if i > 0 and i % 20 == 0:
                await asyncio.sleep(0.2)
        
        # Add small delay between batches to avoid FloodWait
        await asyncio.sleep(RATE_LIMIT)
        
    except FloodWait as e:
        # Handle rate limiting by waiting the required time
        logger.warning(f"FloodWait: Sleeping for {e.value} seconds")
        await asyncio.sleep(e.value)
        # Retry processing the same batch
        await process_single_batch(bot, chat, message_ids, stats)
    except Exception as e:
        logger.error(f"Error processing batch: {e}")
        stats.errors += len(message_ids)
        stats.processed += len(message_ids)


async def update_status(msg, stats):
    """Update status message with current progress"""
    try:
        can = [[InlineKeyboardButton('Cancel', callback_data='index_cancel')]]
        reply = InlineKeyboardMarkup(can)
        await msg.edit_text(
            text=stats.format_stats(),
            reply_markup=reply
        )
    except Exception as e:
        logger.error(f"Error updating status: {e}")


async def batch_index_files(lst_msg_id, chat, msg, bot):
    """Index files strictly in sequential order with optimized batch processing"""
    stats = IndexStats()
    stats.start()
    temp.CANCEL = False
    
    async with lock:
        try:
            start_id = temp.CURRENT
            end_id = lst_msg_id
            
            # Get all message IDs to process (in strict order)
            message_ids = list(range(start_id, end_id + 1))
            total_messages = len(message_ids)
            
            # Set up progress tracking
            update_interval = max(min(total_messages // 10, 50), 1)  # Update at most 10 times, min every 50 messages
            last_update = 0
            
            # Create batches while preserving order
            batches = [message_ids[i:i + BATCH_SIZE] for i in range(0, len(message_ids), BATCH_SIZE)]
            
            # Process each batch strictly in order (no parallel processing)
            for batch_idx, batch in enumerate(batches):
                if temp.CANCEL:
                    stats.is_cancelled = True
                    break
                
                # Process one batch at a time to maintain strict order
                await process_single_batch(bot, chat, batch, stats)
                
                # Update status periodically
                if stats.processed - last_update >= update_interval:
                    last_update = stats.processed
                    await update_status(msg, stats)
                    
                    # Small yield to allow other tasks to run (UI updates, etc.)
                    await asyncio.sleep(0.01)
            
            # Final status update
            if stats.is_cancelled:
                await msg.edit_text(f"Indexing cancelled!\n\n{stats.format_stats()}")
            else:
                await msg.edit_text(f"Indexing completed!\n\n{stats.format_stats()}")
                
        except Exception as e:
            logger.exception(e)
            await msg.edit(f'Error: {e}')
