from typing import Union
from fastapi import FastAPI
import logging

logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World from app 1"}

@app.get("/static/homepage")
def get_static_homepage():
    logger.info(f"request / endpoint!")
    return {"Homepage": "Getting homepage from app 1"}

@app.get("/static/{static_path_asset}")
def get_static_asset(static_path_asset):
    return {"static asset": static_path_asset}