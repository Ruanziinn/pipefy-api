from fastapi import FastAPI
from app.routers import cards

app = FastAPI()

app.include_router(cards.router)


