from pydantic import BaseModel

class UserSchema(BaseModel):
    username : str
    email :str
    name : str
    phone_number : int

    class Config:
        orm_mode = True

class OtpSchema(BaseModel):

    otp : int
    user_id :int

class ChatSchema(BaseModel):
    user_id:int

class MessageSchema(BaseModel):
    user_id : int
    chat_id : int

class LoginSchema(BaseModel):
    email:str

class OtpSchema(BaseModel):
    otp:int


class Settings(BaseModel):
    authjwt_secret_key:str='b4bb9013c1c03b29b9311ec0df07f3b0d8fd13edd02d5c45b2fa7b86341fa405'

class MessageSchema(BaseModel):
    msg:str
    