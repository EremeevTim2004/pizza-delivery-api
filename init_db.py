from database import engine
from databse import Base

from models import User
from models import Order

Base.metadata.create_all(bind=engine)