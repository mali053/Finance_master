from enum import Enum
from pymongo import MongoClient
import os

# Establishing a connection to the MongoDB database using the connection string from the environment variables.
client = MongoClient(os.getenv('DB_CONNECTION_STRING'))

# Creating or accessing the "finance_master" database in the MongoDB instance.
my_db = client['finance_master']


# Defining an enumeration for collections in the database.
class Collections(Enum):
    """
    Enumerates the collections in the database.
    """
    users = my_db['users']
    expenses = my_db['expenses']
    revenues = my_db['revenues']
