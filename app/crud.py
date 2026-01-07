from sqlalchemy.orm import Session
from . import models, schemas, utils

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    # Если пользователь уже существует, возвращаем None
    db_user = get_user_by_username(db, username=user.username)
    if db_user:
        return None
    
    hashed_password = utils.hash_password(user.password)

    db_user = models.User(
        username=user.username,
        password=hashed_password,
        is_active=True
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
