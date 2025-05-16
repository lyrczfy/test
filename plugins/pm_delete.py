from pyrogram import Client, filters
import asyncio

# Settings
DELETE_DELAY = 3  # Delay before deleting the message (set to 0 for instant delete)
SEND_WARNING = True  # Set to True if you want to warn users before deletion

@Client.on_message(
    filters.private & 
    ~filters.me &  # Exclude messages sent by the bot itself
    (filters.document | filters.photo | filters.video | filters.audio | 
     filters.animation | filters.voice | filters.sticker) &
    (filters.forwarded | filters.incoming)  # Also delete forwarded media
)
async def delete_media(client, message):
    try:
        user_id = message.from_user.id if message.from_user else "Unknown"

        if SEND_WARNING:
            warning_msg = await message.reply_text(
                "⚠️ **Media files are not allowed in this chat.**\n"
                "Your message will be automatically deleted.",
                quote=True
            )
            await asyncio.sleep(DELETE_DELAY)  # Wait before deleting
        
        await message.delete()  # Delete the media message
        
        if SEND_WARNING:
            await warning_msg.delete()  # Delete the warning message
        
        print(f"Deleted media message from user {user_id}")
    
    except Exception as e:
        print(f"Error deleting message: {e}")
