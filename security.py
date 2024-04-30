import requests
from requests.auth import HTTPBasicAuth
from schema.schema_users import list_users
from mongo.config.database import user_collection


def login(email, password):
    find = list_users(user_collection.find())

    email_find = find["email": email]
    if email_find == True:
        password_find = find["password": password]
        auth = HTTPBasicAuth(email, password)
        return auth
    else:
        print('erro')


print(requests.get('https://httpbin.org/basic-auth/user/pass', auth=auth))


async def get_users():
    users = list_users(user_collection.find())
    return users
