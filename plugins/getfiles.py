from utils import temp
from imdb import Cinemagoer
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import POST_CHANNELS
from utils import get_poster

# Initialize IMDb API
ia = Cinemagoer()

# Function to search for movies on IMDb
async def search_movies(query):
    try:
        movies = ia.search_movie(query)
        if movies:
            return [{'id': movie.movieID, 'title': movie.get('title', 'Unknown'), 'year': movie.get('year', 'N/A')} for movie in movies[:50]]
        return None
    except Exception as e:
        print(f"[ERROR] IMDb Search Failed: {e}")
        return None

@Client.on_message(filters.command('getfile'))
async def getfile(client, message):
    try:
        query = message.text.split(" ", 1)
        if len(query) < 2:
            return await message.reply_text("<b>Usage:</b> /getfile <movie_name>\n\nExample: /getfile Money Heist")
        
        file_name = query[1].strip()
        movie_results = await search_movies(file_name)

        if not movie_results:
            return await message.reply_text(f"No results found for <b>{file_name}</b> on IMDb.")

        buttons = [
            [InlineKeyboardButton(f"{result['title']} ({result['year']})", callback_data=f"movie_{result['id']}_{file_name}")]
            for result in movie_results
        ]
        reply_markup = InlineKeyboardMarkup(buttons)

        await message.reply_text(
            "🎬 <b>Select the correct movie from the list below:</b>",
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    except Exception as e:
        await message.reply_text(f"⚠️ Error: {str(e)}")

@Client.on_callback_query(filters.regex(r'^movie_'))
async def select_movie(client, callback_query):
    try:
        data = callback_query.data.split('_')
        movie_id, file_name = data[1], '_'.join(data[2:])
        movie_details = ia.get_movie(movie_id)

        if not movie_details:
            return await callback_query.message.reply_text("No details found for this movie.")

        movie_title = movie_details.get('title', 'Unknown')
        languages = movie_details.get('languages', ['N/A'])
        genres = movie_details.get('genres', ['N/A'])
        year = movie_details.get('year', 'N/A')
        kind = movie_details.get('kind', 'N/A')
        url = f"https://www.imdb.com/title/tt{movie_id}/"

        # Custom Telegram link based on file name
        custom_link = f"https://t.me/{temp.U_NAME}?start=getfile-{file_name.replace(' ', '-').lower()}"
        download_button = InlineKeyboardMarkup([
            [InlineKeyboardButton("Click Here To Download", url=custom_link)]
        ])

        confirm_buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("✅ Yes", callback_data=f"post_yes_{movie_id}_{file_name}"),
             InlineKeyboardButton("❌ No", callback_data=f"post_no_{movie_id}")]
        ])

        caption = (
            f"<b>✅ {movie_title} ({year}) #{kind.replace(' ','').upper()}</b>\n\n"
            f"<blockquote>🎙️ {', '.join(languages)}</blockquote>\n\n"
            f"<b>⭐ <a href='{url}'>IMDb Info</a></b>\n"
            f"🎬 <b>Genres:</b> {', '.join(genres)}"
        )

        await callback_query.message.edit_text(caption, reply_markup=download_button, disable_web_page_preview=True, parse_mode=enums.ParseMode.HTML)

        await callback_query.message.reply_text("Do you want to post this movie on channels?", reply_markup=confirm_buttons)

    except Exception as e:
        await callback_query.message.reply_text(f"⚠️ Error: {str(e)}")

@Client.on_callback_query(filters.regex(r'^post_(yes|no)_'))
async def post_to_channels(client, callback_query):
    data = callback_query.data.split('_')
    action, movie_id = data[1], data[2]
    file_name = '_'.join(data[3:]) if len(data) > 3 else None
    
    if action == "yes":
        try:
            movie_details = ia.get_movie(movie_id)
            if not movie_details:
                return await callback_query.message.reply_text(f"No details found for movie ID {movie_id}.")

            movie_title = movie_details.get('title', 'Unknown')
            languages = movie_details.get('languages', ['N/A'])
            genres = movie_details.get('genres', ['N/A'])
            year = movie_details.get('year', 'N/A')
            kind = movie_details.get('kind', 'N/A')
            url = f"https://www.imdb.com/title/tt{movie_id}/"

            # Custom Telegram link based on file name
            custom_link = f"https://t.me/{temp.U_NAME}?start=getfile-{file_name.replace(' ', '-').lower()}" if file_name else "#"
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton("Click Here To Download", url=custom_link)]
            ])

            caption = (
                f"<b>✅ {movie_title} ({year}) #{kind.replace(' ','').upper()}</b>\n\n"
                f"<blockquote>🎙️ {', '.join(languages)}</blockquote>\n\n"
                f"<b>⭐ <a href='{url}'>IMDb Info</a></b>\n"
                f"🎬 <b>Genres:</b> {', '.join(genres)}"
            )

            for channel_id in POST_CHANNELS:
                try:
                    await client.send_message(chat_id=channel_id, text=caption, reply_markup=reply_markup, disable_web_page_preview=True, parse_mode=enums.ParseMode.HTML)
                except Exception as e:
                    await callback_query.message.reply_text(f"⚠️ Error posting to channel {channel_id}: {str(e)}")
            
            await callback_query.message.edit_text("✅ Movie details successfully posted to channels.")
        except Exception as e:
            await callback_query.message.reply_text(f"⚠️ Error: {str(e)}")

    elif action == "no":
        await callback_query.message.edit_text("❌ Movie details will not be posted to channels.")
        
