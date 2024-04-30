from routes.imports_routes import APIRouter, Users, user_collection, \
    list_users, check_login


router_users = APIRouter(prefix="/user")


tags_metadata = [
    {
        "name": "users",
        "description":
            "Operations with users. The **login** logic is also here"
    },
],


@router_users.get("/list/", tags=["users"])
async def get_users():
    users = list_users(user_collection.find())
    return users


@router_users.post("/register/", tags=["users"])
async def create_users(user: Users):
    user_collection.insert_one(dict(user))


@router_users.post("/login/", tags=["users"])
async def login(email, password):
    response = check_login(email, password)
    return response
