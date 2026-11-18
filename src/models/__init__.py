from sqlalchemy import create_engine
import pymysql
from sqlalchemy.orm import sessionmaker, declarative_base






engine = create_engine('mysql+pymysql://root@localhost:3306/facturapp_25T4?charset=utf8mb4', echo=True)
connection = engine.connect()

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()

Base.metadata.blind = engine

