import os
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, KeyboardBuilder
from dotenv import load_dotenv
from database import database as db

load_dotenv('.env')
dbname = os.getenv('DBNAME')
dbuser = os.getenv('DBUSER')
dbpassword = os.getenv('DBPASSWORD')
