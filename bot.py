from aiogram import executor , Dispatcher, types, Bot
import cyrtranslit
from uzwords import words
from imlobot import checkword,chekworduz




API_TOKEN = "6200618543:AAFTP8bncfdkIscob0_lJ-OPkWXckd_F-2c"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def salomlash(message:types.Message):
    await message.reply("Assalomu alaykum, Xush kelibsiz😊")

@dp.message_handler(commands='help')
async def yordam(message: types.Message):
    await message.reply("Botga bilan biror so'z kiriting! kril yoki lotin harflari bilan \nAgar bir nechta so'zlar kiritmoqchi bulsangiz bitta probel tashab yozing")

@dp.message_handler()
async def check_suz(message: types.Message):
    word = message.text.split(" ")
    for w in word:
        if w.isascii():
            result = chekworduz(w)
            if result['aviable']:
                response = f"✅{w.capitalize()}"

            else:
                response = f"❌{w.capitalize()}\n"
                for text in result['matches']:
                    response += f"✅{text.capitalize()}\n"

        else:
            result = checkword(w)
            if result['aviable']:
                response = f"✅{w.capitalize()}"

            else:
                response = f"❌{w.capitalize()}\n"
                for text in result['matches']:
                    response += f"✅{text.capitalize()}\n"

        await message.answer(response)

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)






