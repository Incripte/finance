from fastapi import APIRouter
from models.model_users import Users
from models.model_finances import Finances
from mongo.config.database import user_collection, finances_collection
from schema.schema_users import list_users, check_login
from schema.schema_finances import list_expenses, list_incomes
# from bson import ObjectId