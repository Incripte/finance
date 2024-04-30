from pymongo import MongoClient


client = MongoClient(
    'mongodb+srv://arthur_silva:SiXEK5SCsNLhhPc2QcSAdxZJ4cXuckrN@'
    'cluster0.v8dnhsw.mongodb.net/'
        )  # type: ignore


db = client.local_db


user_collection = db["users_collection"]
finances_collection = db["finances_collection"]
