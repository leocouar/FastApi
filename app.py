from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from config.db import SessionLocal
from schemas.user import User
from models.User import Users
from services import userServices as us

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#USERS
@app.post("/users/", response_model=User)
def create_user(user: User, db: Session = Depends(get_db)):
    db_user = us.get_user_by_Username(db, Username=user.Username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return us.create_user(db=db, user=user)

@app.get("/users/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = us.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = us.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    us.delete_user(db,user_id=user_id)
    return {"message": "Item deleted successfully"}