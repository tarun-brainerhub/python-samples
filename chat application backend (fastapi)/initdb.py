from db import engine
from model import Base

Base.metadata.create_all(engine)