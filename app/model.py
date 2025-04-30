from sqlalchemy import Integer,String,Column,ForeignKey
#my local database file se base ko import kiya
from .database import Base
from sqlalchemy.orm import relationship

#defines the structure of table we want to create in DB and use 
class Blog(Base):
    __tablename__ = "blog"
    #index true telle sqlAchemy that we can use this prop to search and makes searching ,filtering significantly faster.
    id = Column(Integer , primary_key=True , index=True)
    title = Column(String)
    body = Column(String)
    user_id =Column(Integer , ForeignKey('user.id'))
    #users beacuse of tablename

    creator = relationship("User",back_populates="blogs")



class User(Base):
    __tablename__="user"
    id = Column(Integer , primary_key=True,index=True)
    username = Column(String)
    password = Column(String)

    blogs = relationship("Blog" , back_populates= "creator")
    