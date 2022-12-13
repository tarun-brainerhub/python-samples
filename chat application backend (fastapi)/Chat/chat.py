from sqlalchemy.orm import Session
from fastapi import APIRouter,WebSocket, WebSocketDisconnect, Depends
from .wsocket import ConnectionManager
from model import *
import json
from db import SessionLocal
from starlette.requests import Request
from schemas import *


chat_router=APIRouter(
    prefix='/chat',
    tags=['chat']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

manager = ConnectionManager()

@chat_router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket,client_id):
    await manager.connect(websocket)
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    try:
        while True:
            data = await websocket.receive_text()
            # await manager.send_personal_message(f"You wrote: {data}", websocket)
            message = {"time":current_time,"clientId":client_id,"message":data}
            await manager.broadcast(json.dumps(message))

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        message = {"time":current_time,"clientId":client_id,"message":"Offline"}
        await manager.broadcast(json.dumps(message))

@chat_router.post("/chat/")
def chat(msg:MessageSchema,request: Request,db: Session = Depends(get_db)):
            email = request.session.get("email", None)
            print(email)
            db_user = db.query(User).filter(User.email==email).first()
            db_chat_exist =db.query(Chat).filter(Chat.user_id == db_user.user_id).first()
            if not db_chat_exist:
                db_chat = Chat(user_id=db_user.user_id)
                db.add(db_chat)
                db.commit()
            db_chat = db.query(Chat).filter(Chat.user_id == db_user.user_id).first()
            if db_chat:
                db_message = Message(text=msg.msg,user_id =db_user.user_id,chat_id =db_chat.chat_id)
                db.add(db_message)
                db.commit()
            return f'{msg.msg}'

@chat_router.get("/chat/{id}")
def get_chat(id:int,request: Request,db: Session = Depends(get_db)):
    email = request.session.get("email", None)
    db_user = db.query(User).filter(User.email==email).first()
