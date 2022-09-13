import os
import asyncio
from googletrans import Translator
from pyrogram import Client, filters
from pyrogram.types import (InlineQuery,
                            InputTextMessageContent,
                            InlineQueryResultArticle,
                            InlineKeyboardButton,
                            InlineKeyboardMarkup
                            )


if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config


mozhi = Client(
    name="mozhi",
    bot_token=Config.TG_BOT_TOKEN,
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
)


"""Function for start message"""
@mozhi.on_message(filters.command(["start", "help"]))
async def start_bot(_, m):
    translator = Translator()
    text = "നമസ്കാരം {}\nഞാൻ ഒരു മലയാളം വിവർത്തക ബോട്ട് ആണ്. കൂടുതൽ അറിയുവാൻ എന്റെ ടെലിഗ്രാം <a href='{}'>ചാനൽ</a> സന്ദർശിക്കുക."
    await m.reply_text(
        text=text.format(m.from_user.mention, 't.me/rmprojects'),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("♨️ Source", url="https://github.com/m4mallu/mozhi"),
                    InlineKeyboardButton("🔎  Translate", switch_inline_query_current_chat='')
                ]
            ]
        )
    )


"""Function for inline query"""
@mozhi.on_inline_query()
async def inline_replay(_, query: InlineQuery):
    result = ''
    inline_results = []
    #
    string = query.query.strip()
    formatting = "Translation Results for 👉 <b>{}</b> will be...\n\n👉 <code>{}</code>"
    #
    try:
        result = Translator().translate(text=string, dest='ml').text
    except Exception:
        pass
    #
    inline_results.append(
        InlineQueryResultArticle(
            title="Transation Results for 👉 {}".format(string),
            input_message_content=InputTextMessageContent(
                message_text=formatting.format(string, result)),
            thumb_url='https://telegra.ph/file/19008e0b8e4c578fcfd86.png',
            description=result,
        )
    )
    if result:
        try:
            await query.answer(
                results=inline_results,
                cache_time=0,
            )
        except Exception:
            pass


""" If the inline result belongs to a private chat, the bot will delete the message after 15 seconds """
@mozhi.on_message(filters.private & filters.incoming)
async def delete_message(_, m):
    await asyncio.sleep(15)
    await m.delete()


print("\nBot Started Successfully !")
mozhi.run()
