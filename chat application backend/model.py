from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, BIGINT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func, text
from datetime import datetime, timedelta

Base = declarative_base()


class User(Base):
    __tablename__ = "app_user"

    user_id = Column(Integer, primary_key=True, index=True, server_default=text("nextval('app_user_user_id_seq'::regclass)"))
    username = Column(String)
    email = Column(String)
    name = Column(String)
    phone_number =Column(BIGINT)

class Otp(Base):
    __tablename__ = "otp"

    otp_id = Column(Integer, primary_key=True, index=True, server_default=text("nextval('otp_otp_id_seq'::regclass)"))
    otp =Column(Integer)
    otp_exp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('app_user.user_id'))

    app_user =relationship('User')


class Chat(Base):
    __tablename__ = "chat"

    chat_id = Column(Integer, primary_key=True, index=True, server_default=text("nextval('chat_chat_id_seq'::regclass)"))
    time_created =  Column(DateTime, default=datetime.now())
    user_id = Column(Integer, ForeignKey('app_user.user_id'))

    app_user =relationship('User')

class Message(Base):
    __tablename__ = "message"

    message_id = Column(Integer, primary_key=True, index=True, server_default=text("nextval('message_message_id_seq'::regclass)"))
    text = Column(String)
    time_created =  Column(DateTime(timezone=True), server_default=func.now())
 
    user_id = Column(Integer, ForeignKey('app_user.user_id'))
    chat_id = Column(Integer, ForeignKey('chat.chat_id'))

    app_user = relationship('User')
    chat = relationship("Chat")