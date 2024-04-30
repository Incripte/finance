from mongo.config.database import user_collection


#  Regisre a new user
def create_user(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": str(user["name"]),
        "birth": str(user["birth"]),
        "email": str(user["email"]),
        "password": str(user["password"])
    }


#  list users in create users
def list_users(users):
    return [create_user(user) for user in users]


#  Check-credentials to login
def check_login(email, password):
    users = list_users(user_collection.find(
        {"email": email, "password": password})
        )
    check_email = users[0]["email"]
    check_password = users[0]["password"]

    if check_email == email and check_password == password:
        return True
    else:
        return False
