from fastapi import APIRouter
from config.db import conn
from models.User import users
from schemas.user import User
from cryptography.fernet import Fernet

user = APIRouter()

key = Fernet.generate_key()
f= Fernet(key)


@user.get("/users")
async def getUsers():
    return conn.execute(users.select()).fetchall()

@user.post("/users")
def create_user(user: User):
    new_user = {"Username": user.Username, "Fullname": user.Fullname}
    new_user["Password"] = f.encrypt(user.Password.encode("utf-8"))
    result = conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()