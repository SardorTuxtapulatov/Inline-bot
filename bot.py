import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from my_keyboards import menu_button
from aiogram.client.session.aiohttp import AiohttpSession

session = AiohttpSession(proxy='http://proxy.server:3128')

ADMIN = 6066474564 # Bu yerga id kiriting
TOKEN = "7159302365:AAEuD0BTw0VX9Or-Nd8Ng4Oaclyw9LA7j38" #Token kiriting
dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML,session=session)




@dp.message(CommandStart())
async def command_start_handler(message: Message,state:FSMContext) -> None:
    full_name = message.from_user.full_name
    text = f"Assalomu alaykum,{full_name} Sifat Maktablar botiga hush kelibsiz\nBu yerda maktablar haqida ma'lumot olishingiz mumkin!"
    await message.answer(text=text,reply_markup=menu_button)


#maktab tugmasi bosilganda yuboriladigon habar
@dp.message(F.text=="Maktab 🎒")
async def maktab_menu(message:Message,state:FSMContext):
    #maktabingiz haqida ma'lumot
    text = """Maktab 1978- yil Zomin tumanga qarashli 39-maktab ochilgan. Maktab moslashtirilgan binoda joylashgan. Unga 130 ta 15 ta o’qituvchi maktab direktorii Nurmatov I.

     1979- yil 1- sentyabrdan Yangi qurilgan binoda 200 o’quvchi 20 nafar o’qiituvchi ko’p millatli maktab bo’lib asosiy o’quvchilarni rusiyzabon o’quvchilar tashkil etilgan.

     Maktab direktori:  Baratov Bolbek  Umarovich. 1980-yildan boshlab maktab  10-yillik bo’lib maktabda 400 o’quvchi 40 nafar o’qituvchi faoliyat ko’rsatgan.

         Maktab direktori:  Eshboev Mamat

1981- yildan boshlab maktab direktori:  Tovboev Bosim  360 nafar o’quvchi 45 nafar o’qituvchi faoliyat ko’rsatgan."""
    #maktab rasmini olish 
    photo = types.FSInputFile("maktab.jpg",filename="maktab.jpg")
    
    #maktab haqidagi ma'lumotni yuborish
    await message.answer_photo(photo=photo,caption=text)


@dp.message(F.text=="Biz haqimizda👨🏻‍💻")
async def maktab_menu(message:Message,state:FSMContext):
    #maktabingiz haqida ma'lumot
    text = """Maktab 1978- yil Zomin tumanga qarashli 39-maktab ochilgan. Maktab moslashtirilgan binoda joylashgan. Unga 130 ta 15 ta o’qituvchi maktab direktorii Nurmatov I.

     1979- yil 1- sentyabrdan Yangi qurilgan binoda 200 o’quvchi 20 nafar o’qiituvchi ko’p millatli maktab bo’lib asosiy o’quvchilarni rusiyzabon o’quvchilar tashkil etilgan.

     Maktab direktori:  Baratov Bolbek  Umarovich. 1980-yildan boshlab maktab  10-yillik bo’lib maktabda 400 o’quvchi 40 nafar o’qituvchi faoliyat ko’rsatgan.

         Maktab direktori:  Eshboev Mamat

1981- yildan boshlab maktab direktori:  Tovboev Bosim  360 nafar o’quvchi 45 nafar o’qituvchi faoliyat ko’rsatgan."""
    #maktab rasmini olish 
    photo = types.FSInputFile("bizhaqimizda.jpg",filename="bizhaqimizda.jpg")
    
    #maktab haqidagi ma'lumotni yuborish
    await message.answer_photo(photo=photo,caption=text)


@dp.message(F.text=="Maktab 🎒2")
async def maktab_menu(message:Message,state:FSMContext):
    #maktabingiz haqida ma'lumot
    text = """22Maktab 1978- yil Zomin tumanga qarashli 39-maktab ochilgan. Maktab moslashtirilgan binoda joylashgan. Unga 130 ta 15 ta o’qituvchi maktab direktorii Nurmatov I.

     1979- yil 1- sentyabrdan Yangi qurilgan binoda 200 o’quvchi 20 nafar o’qiituvchi ko’p millatli maktab bo’lib asosiy o’quvchilarni rusiyzabon o’quvchilar tashkil etilgan.

     Maktab direktori:  Baratov Bolbek  Umarovich. 1980-yildan boshlab maktab  10-yillik bo’lib maktabda 400 o’quvchi 40 nafar o’qituvchi faoliyat ko’rsatgan.

         Maktab direktori:  Eshboev Mamat

1981- yildan boshlab maktab direktori:  Tovboev Bosim  360 nafar o’quvchi 45 nafar o’qituvchi faoliyat ko’rsatgan."""
    #maktab rasmini olish 
    photo = types.FSInputFile("maktab.jpg",filename="maktab.jpg")
    
    #maktab haqidagi ma'lumotni yuborish
    await message.answer_photo(photo=photo,caption=text)


@dp.message(F.text=="Maktab 🎒3")
async def maktab_menu(message:Message,state:FSMContext):
    #maktabingiz haqida ma'lumot
    text = """33Maktab 1978- yil Zomin tumanga qarashli 39-maktab ochilgan. Maktab moslashtirilgan binoda joylashgan. Unga 130 ta 15 ta o’qituvchi maktab direktorii Nurmatov I.

     1979- yil 1- sentyabrdan Yangi qurilgan binoda 200 o’quvchi 20 nafar o’qiituvchi ko’p millatli maktab bo’lib asosiy o’quvchilarni rusiyzabon o’quvchilar tashkil etilgan.

     Maktab direktori:  Baratov Bolbek  Umarovich. 1980-yildan boshlab maktab  10-yillik bo’lib maktabda 400 o’quvchi 40 nafar o’qituvchi faoliyat ko’rsatgan.

         Maktab direktori:  Eshboev Mamat

1981- yildan boshlab maktab direktori:  Tovboev Bosim  360 nafar o’quvchi 45 nafar o’qituvchi faoliyat ko’rsatgan."""
    #maktab rasmini olish 
    photo = types.FSInputFile("maktab.jpg",filename="maktab.jpg")
    
    #maktab haqidagi ma'lumotni yuborish
    await message.answer_photo(photo=photo,caption=text)


@dp.message(F.text=="Maktab 🎒4")
async def maktab_menu(message:Message,state:FSMContext):
    #maktabingiz haqida ma'lumot
    text = """444Maktab 1978- yil Zomin tumanga qarashli 39-maktab ochilgan. Maktab moslashtirilgan binoda joylashgan. Unga 130 ta 15 ta o’qituvchi maktab direktorii Nurmatov I.

     1979- yil 1- sentyabrdan Yangi qurilgan binoda 200 o’quvchi 20 nafar o’qiituvchi ko’p millatli maktab bo’lib asosiy o’quvchilarni rusiyzabon o’quvchilar tashkil etilgan.

     Maktab direktori:  Baratov Bolbek  Umarovich. 1980-yildan boshlab maktab  10-yillik bo’lib maktabda 400 o’quvchi 40 nafar o’qituvchi faoliyat ko’rsatgan.

         Maktab direktori:  Eshboev Mamat

1981- yildan boshlab maktab direktori:  Tovboev Bosim  360 nafar o’quvchi 45 nafar o’qituvchi faoliyat ko’rsatgan."""
    #maktab rasmini olish 
    photo = types.FSInputFile("maktab.jpg",filename="maktab.jpg")
    
    #maktab haqidagi ma'lumotni yuborish
    await message.answer_photo(photo=photo,caption=text)

@dp.message(F.text=="Maktab 🎒5")
async def maktab_menu(message:Message,state:FSMContext):
    #maktabingiz haqida ma'lumot
    text = """555Maktab 1978- yil Zomin tumanga qarashli 39-maktab ochilgan. Maktab moslashtirilgan binoda joylashgan. Unga 130 ta 15 ta o’qituvchi maktab direktorii Nurmatov I.

     1979- yil 1- sentyabrdan Yangi qurilgan binoda 200 o’quvchi 20 nafar o’qiituvchi ko’p millatli maktab bo’lib asosiy o’quvchilarni rusiyzabon o’quvchilar tashkil etilgan.

     Maktab direktori:  Baratov Bolbek  Umarovich. 1980-yildan boshlab maktab  10-yillik bo’lib maktabda 400 o’quvchi 40 nafar o’qituvchi faoliyat ko’rsatgan.

         Maktab direktori:  Eshboev Mamat

1981- yildan boshlab maktab direktori:  Tovboev Bosim  360 nafar o’quvchi 45 nafar o’qituvchi faoliyat ko’rsatgan."""
    #maktab rasmini olish 
    photo = types.FSInputFile("maktab.jpg",filename="maktab.jpg")
    
    #maktab haqidagi ma'lumotni yuborish
    await message.answer_photo(photo=photo,caption=text)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())