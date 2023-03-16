from sqlalchemy.orm import Session
from models.User import Users
from schemas.user import User
from cryptography.fernet import Fernet
from werkzeug.security import generate_password_hash,check_password_hash

def get_user(db: Session, user_id: int):
    return db.query(Users).filter(Users.Id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Users).offset(skip).limit(limit).all()

def get_user_by_Username(db: Session, Username: str):
    return db.query(Users).filter(Users.Username == Username).first()

def create_user(db: Session,user: User):
    # password = f.encrypt(user.Password.encode("utf-8"))
    password = generate_password_hash(user.Password)
    db_user = Users(Username = user.Username, Fullname= user.Fullname ,Password= password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session,Users:Users):
    db.delete(Users)
    db.commit()
    pass

def decrypt(hash,password):
    x = check_password_hash(hash,password)
    return x