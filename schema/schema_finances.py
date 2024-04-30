def add_incomes(income) -> dict:
    return {
        "id": str(income["_id"]),
        "title": str(income["title"]),
        "description": str(income["description"]),
        "type": str(income["type"]),
        "value": float(income["value"]),
        "date": str(income["date"]),
    }


def list_incomes(incomes):
    return [add_incomes(income) for income in incomes]


def add_expenses(expense) -> dict:
    neg_value = float(expense["value"] * -1)
    return {
        "id": str(expense["_id"]),
        "title": str(expense["title"]),
        "description": str(expense["description"]),
        "type": str(expense["type"]),
        "value": neg_value,
        "date": str(expense["date"]),
    }


def list_expenses(expenses):
    return [add_expenses(expense) for expense in expenses]
