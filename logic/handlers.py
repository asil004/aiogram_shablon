import os
from aiogram import types, Bot
from aiogram.fsm.state import StatesGroup, State
from dotenv import load_dotenv
from database import database as db
from aiogram.fsm.context import FSMContext

load_dotenv('.env')

dbname = os.getenv('DBNAME')
dbuser = os.getenv('DBUSER')
dbpassword = os.getenv('DBPASSWORD')
SUPER_ADMIN = int(os.getenv('ADMIN'))
