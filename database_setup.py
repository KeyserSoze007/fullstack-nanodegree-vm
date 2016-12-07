import os
import sys

from sqlalchemy import Column,ForeignKey,Integer,String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base=declarative_base()

class Resturant(Base):
    __tablename__='resturant'
    name=Column(String(80),nullable=False)
    id=Column(Integer,primary_key=True)


class MenuItem(Base):
    __tablename__='menu_item'
    name=Column(String(80),nullable=False)
    id=Column(Integer,primary_key=True)
    course=Column(String(250))
    description=Column(String(8))
    price=Column(String(8))
    resturant_id=Column(Integer, ForeignKey('resturant.id'))
    resturant=relationship(Resturant)



engine=create_engine('sqlite:///resturantmenu.db')

Base.metadata.create_all(engine)
