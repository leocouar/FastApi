from config.db import meta, engine
from sqlalchemy import Column, Integer, Numeric, String, Table

users = Table(
    "users",meta,
    Column("id", Integer, primary_key=True),
    Column("Username",String(50), nullable=False),
    Column("Fullname",String(200)),
    Column("Password",String(120), nullable=False),
    Column("IsAdmin",Numeric))

meta.create_all(engine)