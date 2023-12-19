from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, default=None)
    last_name = Column(String, default=None)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    otp = Column(Integer)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<User {self.email}>"


class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True, index=True)
    bio = Column(String(500))
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), unique=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    # Relationships
    user = relationship("User", lazy="joined")

    def __repr__(self):
        return f"<User {self.user.first_name} {self.user.last_name}>"
