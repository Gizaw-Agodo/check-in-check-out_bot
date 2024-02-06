import telegram
import schedule
import asyncio
from telegram import Bot
import asyncio
from dotenv import load_dotenv



# Telegram bot API token
TOKEN = ''
GROUP_ID = ""
bot = telegram.Bot(token=TOKEN)


async def send_check_in_reminder():
    message = "📢🕒 Good evening A2SV heads! \n It's time to check in for today's remote education session.\n Check in now! 💻🌟"
    await bot.send_message(chat_id=GROUP_ID, text=message)


async def send_check_out_reminder():
    message = "🌙🔚 Good evening A2SV heads!\n it's time to check out.\n Check out now and have a restful evening! 😊🌟"
    await bot.send_message(chat_id=GROUP_ID, text=message)

    
async def scheduler():
    schedule.every().day.at("23:05").do(lambda: asyncio.create_task(send_check_in_reminder()))
    schedule.every().day.at("10:27").do(lambda: asyncio.create_task(send_check_out_reminder()))

    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

async def main():
    await scheduler()

if __name__ == "__main__":
    asyncio.run(main())
