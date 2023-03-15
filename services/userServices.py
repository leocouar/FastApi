from sqlalchemy.orm import Session
from models.User import Users
from schemas.user import User
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f= Fernet(key)

def get_user(db: Session, user_id: int):
    return db.query(Users).filter(Users.Id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Users).offset(skip).limit(limit).all()

def get_user_by_Username(db: Session, Username: str):
    return db.query(Users).filter(Users.Username == Username).first()

def create_user(db: Session,user: User):
    password = f.encrypt(user.Password.encode("utf-8"))
    db_user = Users(Username = user.Username, Fullname= user.Fullname ,Password= password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    user = db.query(Users).filter(Users.Id == user_id).first()
    db.delete(user)
    db.commit()
    return user