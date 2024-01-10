from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config_loader import load_config
from middlewares.ProcessTimeHeader import add_process_time_header
from routes import include_router

config = load_config()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=config['server']['cors'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(add_process_time_header)

include_router(app, config)
