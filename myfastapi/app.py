from fastapi import FastAPI
from myfastapi.routes.setup import router as api_router

# Create an instance of the FastAPI class
app = FastAPI()

app.include_router(api_router)
