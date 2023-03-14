from fastapi import APIRouter
from config.db import conn
from models.User import users

user = APIRouter()


@user.get("/users")
async def getUsers():
    return conn.execute(users.select()).fetchall()