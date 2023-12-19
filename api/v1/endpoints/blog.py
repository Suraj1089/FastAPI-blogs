from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from db.schemas.blogs import PostCreate

router = APIRouter(
    prefix='/blogs',
    tags=['blogs']
)


@router.post('/')
def create_blog(post: PostCreate, db: Session = Depends(get_db)):
    return post


@router.get('/')
def get_blog():
    pass
