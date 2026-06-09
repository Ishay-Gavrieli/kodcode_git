from fastapi import FastAPI
from routers import router


app = FastAPI()

# app.include_router(router, prefix="/soldiers")


app.include_router(router)