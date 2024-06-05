from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine=create_engine('postgresql://postgres:eremeevt2004@loacalhost/pizza_dilivery',
    echo=True
)
Base=declarative_base()
Session=sessionmaker()
