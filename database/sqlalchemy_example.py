#!/usr/bin/env python3

from sqlalchemy import create_engine, text, String, Integer, Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Player(Base):
    __tablename__ = "player"
    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    number = Column(Integer)
    position = Column(String(2))


# In-memory database with an sqlite backend
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
jackie = Player(name="Jackie Robinson", number=42, position="2B")
session.add(jackie)
session.commit()
session.close()
