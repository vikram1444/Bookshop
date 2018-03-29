import os
import sys
from sqlalchemy import Column,ForeignKey,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base=declarative_base()
class Registration(Base):
     __tablename__ = 'registration'
     name = Column('name',String(100),nullable=False)
     phone = Column('phone',String(100),nullable=False)
     order_id=Column('order_id',Integer,primary_key=True)
     count1 = Column('count1',Integer,nullable=False)
     count2 = Column('count2',Integer,nullable=False)
     count3 = Column('count3',Integer,nullable=False)
     count4 = Column('count4',Integer,nullable=False)
     count5 = Column('count5',Integer,nullable=False)
     count6 = Column('count6',Integer,nullable=False)
     count7 = Column('count7',Integer,nullable=False)
     count8 = Column('count8',Integer,nullable=False)
     count9 = Column('count9',Integer,nullable=False)
     count10 = Column('count10',Integer,nullable=False)   
engine=create_engine('sqlite:///regis.db')
Base.metadata.create_all(engine)