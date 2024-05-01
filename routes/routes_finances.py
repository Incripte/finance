from routes.imports_routes import APIRouter, Finances, finances_collection, \
    list_incomes


router = APIRouter(prefix="/finances")


tags_metadata = [
    {
        "name": "finances",
        "description":
            "Operations with finances"
    },
],


# TODO: Preciso pegar incomes e expenses
@router.get("/historic/", tags=["finances"])
async def get_finances():
    return list_incomes(finances_collection.find())


@router.post("/income/", tags=["finances"])
async def post_incomes(income: Finances):
    finances_collection.insert_one(dict(income))


@router.post("/expense/", tags=["finances"])
async def post_expenses(expense: Finances):
    finances_collection.insert_one(dict(expense))
