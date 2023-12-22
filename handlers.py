from telegram import Update
from telegram.ext import CallbackContext
import keyboards
from db import get_phone_by_id


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='salom',
        reply_markup=keyboards.home_keyboard()
    )

def shop(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='start shopping',
        reply_markup=keyboards.brends_keyboard()
    )

def phones(update: Update, context: CallbackContext):
    brend = update.callback_query.data.split(':')[1]

    update.callback_query.message.reply_text(
        text='start shopping',
        reply_markup=keyboards.phones_keyboard(brend)
    )

def phone(update: Update, context: CallbackContext):
    brend, phone_id = update.callback_query.data.split(':')[1].split('-')

    phone_data = get_phone_by_id(brend=brend, doc_id=phone_id)

    update.callback_query.message.reply_photo(
        photo=phone_data['img_url'],
        caption=f'{phone_data["name"]}\n{phone_data["color"]}',
        # reply_markup=keyboards.phones_keyboard(brend)
    )
