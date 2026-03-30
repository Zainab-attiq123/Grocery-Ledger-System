from fastapi import FastAPI
from routes import router

app = FastAPI(title="Grocery Ledger System")

app.include_router(router)