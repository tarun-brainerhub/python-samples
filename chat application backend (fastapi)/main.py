from fastapi import FastAPI
from User.user import auth_router
from Chat.chat import chat_router
from starlette.middleware.sessions import SessionMiddleware
from fastapi_jwt_auth import AuthJWT
from schemas import Settings
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(auth_router)
app.include_router(chat_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, secret_key="SECRET_KEY")


@AuthJWT.load_config
def get_config():
    return Settings()
   
    


