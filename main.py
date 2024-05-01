import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.routes_users import router_users
from routes.routes_finances import router


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou específique os domínios permitidos
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


app.include_router(router_users)
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app)
