from config.db import Base
from sqlalchemy import Column, Integer, Numeric, String, Table

# users = Table(
#     "Users",meta,
#     Column("id", Integer, primary_key=True, autoincrement=True),
#     Column("Username",String(50), nullable=False),
#     Column("Fullname",String(200)),
#     Column("Password",String(220), nullable=False),
#     Column("IsAdmin",Integer))

class Users(Base):
    __tablename__ = 'Users'

    Id = Column(Integer, primary_key=True, unique=True)
    Username = Column(String(50), nullable=False)
    Fullname = Column(String(200))
    Password = Column(String(120), nullable=False)
    IsAdmin = Column(Numeric)
