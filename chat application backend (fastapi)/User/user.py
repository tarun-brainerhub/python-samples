
from fastapi import Depends,status,HTTPException,APIRouter,Header
from typing import Union
from sqlalchemy.orm import Session
from model import *
from schemas import OtpSchema, UserSchema, LoginSchema
from fastapi_jwt_auth import AuthJWT
from fastapi_mail import FastMail, MessageSchema
from .email_conf import conf
from db import SessionLocal
import random
from starlette.requests import Request
from datetime import datetime,timedelta

auth_router=APIRouter(
    prefix='/auth',
    tags=['auth']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@auth_router.get('/')
async def hello(Authorize:AuthJWT=Depends()):

    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )

    return {"message":"Hello World"}

@auth_router.post("/register", status_code = status.HTTP_201_CREATED )
def register_user(user:UserSchema, db: Session = Depends(get_db)):
    db_email=db.query(User).filter(User.email==user.email).first()

    if db_email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with the email already exists"
        )

    db_username=db.query(User).filter(User.username==user.username).first()

    if db_username is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with the username already exists"
        )

    db_number=db.query(User).filter(User.phone_number==user.phone_number).first()
    if db_number is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with the number already exists"
        )

    new_user = User(username = user.username, email= user.email, name = user.name, phone_number = user.phone_number)
    db.add(new_user)
    db.commit()
    return HTTPException(status_code=status.HTTP_201_CREATED,
            detail="User Created"
        )

@auth_router.get("/user/{username}")
def get_user(username:str, db: Session = Depends(get_db)):
    if username:
        user = db.query(User).filter(User.username==username).first()
        db.close() 
        if user:
            return user
        else:
            raise HTTPException(status_code=404, detail="User not found")

@auth_router.get("/users/")
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    if users is None:
        raise HTTPException(status_code=404, detail="User not found")
    return users

@auth_router.post("/login", status_code=status.HTTP_200_OK)
async def send_otp(user:LoginSchema,request: Request,db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email==user.email).first()
    if db_user is None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this Email dose not exists"
        )
    otp_value = str(random.randint(1000 , 9999))
    db_otp = db.query(Otp).filter(Otp.user_id ==db_user.user_id)
    otp_check = db_otp.first()
    if otp_check:
        db_otp.update({"otp":otp_value,"otp_exp":datetime.now() + timedelta(minutes=5)})
        db.commit()
    else:
        db_otp = Otp(otp=otp_value,otp_exp =datetime.now() + timedelta(minutes=5) ,user_id = db_user.user_id)
        # db_otp = Otp(otp=otp_value,user_id = db_user.user_id)
        db.add(db_otp)
        db.commit()
    if db_user:
        message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=[user.email],
        body=f"Your otp is {otp_value}",
        subtype="html"
        )   
        fm = FastMail(conf)
        await fm.send_message(message)
        print(message)
    request.session["email"] = user.dict().get('email')
    return  HTTPException(status_code=status.HTTP_200_OK,
            detail={"data":"email sended","email":user.email}
        )

@auth_router.post("/verify", status_code=200)
async def login(otp:OtpSchema,request: Request, Authorize:AuthJWT=Depends(),db: Session = Depends(get_db),email: Union[str, None] = Header(default=None)):
    # email = request.session.get("email", None)
    print(email)
    db_user = db.query(User).filter(User.email==email).first()
    db_otp = db.query(Otp).filter(Otp.user_id == db_user.user_id)
    otp_check = db_otp.first()
    if otp.otp != otp_check.otp:
        raise HTTPException(status_code=404, detail="Wrong OTP")
    # if otp_check.otp_exp < datetime.now():
    #     db_otp.update({"otp":None})
    #     db.commit()
    #     raise HTTPException(status_code=404, detail="otp Expired")
    if otp_check:
        db_otp.update({"otp":None})
        db.commit()
        access_token=Authorize.create_access_token(subject=db_user.email)
        refresh_token=Authorize.create_refresh_token(subject=db_user.email)
    response={
            "access":access_token,
            "refresh":refresh_token
        }
    return  HTTPException(status_code=status.HTTP_200_OK,
            detail= response
        )
