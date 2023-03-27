from .database import Base
from sqlalchemy import Column, Integer, String



class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)

    # name = Column(String)
    # fullname = Column(String)
    # nickname = Column(String)

    # def __repr__(self):
    #     return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)
