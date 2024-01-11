from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config_loader import load_config
from app.middlewares.ProcessTimeHeader import add_process_time_header
from app.routes import include_router
from app.models.UsersList import UsersList

config = load_config()
userList = UsersList(save_time=config["server"]["life_time"])

app = FastAPI(
    on_startup=[userList.start_cleanup],
    on_shutdown=[userList.stop_cleanup]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config["server"]["cors"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(add_process_time_header)

include_router(app, config, userList)
