from sqlalchemy.orm import Session
from database import User, SessionLocal
from functools import lru_cache

# Dependency to get DB session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD Operations

@lru_cache(maxsize=128)
def create_user(name: str, db: Session):
    user = User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@lru_cache(maxsize=128)
def get_user_by_id(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()

@lru_cache(maxsize=128)
def update_user_name(user_id: int, new_name: str, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.name = new_name
        db.commit()
        return user
    return None

@lru_cache(maxsize=128)
def search_users_by_name(name: str, db: Session):
    users = db.query(User).filter(User.name.like(f'%{name}%')).all()
    return [user.name for user in users]
