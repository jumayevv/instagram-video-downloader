from aiogram import types,executor  
from aiogram.dispatcher.filters import Text
from loader import dp,bot
from insta import insta_downloader

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("* Xush kelibsiz, menga link yuboring *",parse_mode=types.ParseMode.MARKDOWN)



@dp.message_handler(regexp=r'https?://(?:www\.)?instagram\.com/.+')
async def download_instagram_video(message: types.Message):

        try:
            video_link = message.text
            
            last_message= await bot.send_message(message.chat.id,"*serverga yuklanmoqda...*")
            
            data = insta_downloader(link=video_link)
            last_message2 = await bot.send_message(message.chat.id,"*telegramga yuklanmoqda...*")
           # await bot.edit_message_text(text="*telegramga yuklanmoqda...*", chat_id=message.chat.id, message_id=last_message.message_id)
    
            if 'error' in data:
                if 'limit error' in data:
                    await message.answer(text="*Limitingiz tugagan !*",parse_mode=types.ParseMode.MARKDOWN)
                elif 'system error' in data:
                    await message.answer(text="*Tizimda xatolik ! linkni tekshirib boshqattan yuboring*",parse_mode=types.ParseMode.MARKDOWN)
                else:
                    await message.answer(text="*Link yaroqsiz ! boshqattan urinb ko'ring*",parse_mode=types.ParseMode.MARKDOWN)
            else:
                await bot.delete_message(message.chat.id,last_message.message_id)
                if data['type']=='Image':
                    await message.answer_photo(photo=data['media'])
                elif data['type']=='Video':
                    last_message3 = await bot.send_message(message.chat.id,"*Video hajmi biroz katta, ozgina kuting*")
                   
                    await message.answer_video(video=data['media'])

                    await bot.delete_message(message.chat.id,last_message3.message_id)
                elif data['type']=='Multiple-Data':
                    await bot.send_message(message.chat.id,"*Siz yuborgan link orqali bir nechta malumot topildi,ozgina kuting*")
                    for i in data['media']:
                        await message.answer_document(document=i['media'])
                elif data['type']=='Story-Video':
                    await message.answer_video(video=data['media'])
                    
                elif data['type']=='Story-Image':
                    await message.answer_photo(photo=data['media'])
                else:
                    await message.answer(text= "*bu link orqali hech narsa topilmadi !*",parse_mode=types.ParseMode.MARKDOWN)
                
                await bot.delete_message(message.chat.id,last_message2.message_id)

        except Exception:
            await bot.send_message(message.chat.id,"*Tizimda xatolik, qayta urining*")

if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)
    