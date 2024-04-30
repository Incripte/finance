import uvicorn

from fastapi import FastAPI
from routes.routes_users import router_users
from routes.routes_finances import router

app = FastAPI()


app.include_router(router_users)
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app)
