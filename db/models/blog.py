import enum

from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy import Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db.database import Base


class Post(Base):

    __tablename__ = "post"

    class PostChoices(enum.Enum):
        published = "Published"
        unpublished = "Unpublished"

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("author.id"), nullable=False)
    title = Column(String(100), nullable=False)
    summary = Column(String(400))
    content = Column(Text)
    status = Column('status', Enum(PostChoices), default=PostChoices.unpublished)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

    author = relationship("Author")

    def __repr__(self):
        return f'<Post "{self.title}">'


class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)  # FK added
    post_id = Column(Integer, ForeignKey('post.id'), index=True, nullable=False)
    upvotes = Column(Integer, default=0)
    content = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

    # Relationships
    user = relationship("User")
    post = relationship("Post")

    def __repr__(self):
        return f'<Comment "{self.content[:20]}...">'


class Like(Base):
    __tablename__ = "like"
    id = Column(Integer, primary_key=True)
