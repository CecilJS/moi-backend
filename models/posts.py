from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from core.database import Base

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    body: Mapped[str] = mapped_column()

    comments: Mapped[List["Comment"]] = relationship(back_populates="post")