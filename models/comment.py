from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from core.database import Base

class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    body: Mapped[str] = mapped_column()
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))

    post: Mapped["Post"] = relationship(back_populates="comments")
