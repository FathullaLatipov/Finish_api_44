from fastapi import FastAPI

from user.user_api import user_router
from transfers.transfers_api import transfer_router

# Создать базу
from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(user_router)
app.include_router(transfer_router)

@app.get('/home')
async def home():
    return {'message': 'hello this is home'}
