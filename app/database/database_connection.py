from enum import Enum
from pymongo import MongoClient
import os

client = MongoClient(os.getenv('DB_CONNECTION_STRING'))
my_db = client['finance_master']


class Collections(Enum):
    users = my_db['users'],
    expenses = my_db['expenses'],
    revenues = my_db['revenues']
