from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

reg_menu = InlineKeyboardMarkup()
reg_menu.add(InlineKeyboardButton(
    text='registration', callback_data='reg'
))

options = InlineKeyboardMarkup()
options.add(
    InlineKeyboardButton(
        text='Qizlar', callback_data='Qizlar'
    ),
    InlineKeyboardButton(
        text='Er-jigitler', callback_data='Er-jigitler'
    )
)

menu = InlineKeyboardMarkup()
menu.add(InlineKeyboardButton(
    text='menu', callback_data='menu'
))
