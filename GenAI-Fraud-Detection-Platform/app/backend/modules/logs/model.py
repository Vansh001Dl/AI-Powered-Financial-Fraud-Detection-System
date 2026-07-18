from sqlalchemy import ForeignKey, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.backend.common.mixins import TimestampMixin, UUIDPrimaryKeyMixin
from app.backend.db.base import Base


class AppLog(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "logs"

    project_id: Mapped[str | None] = mapped_column(ForeignKey("projects.id"))
    user_id: Mapped[str | None] = mapped_column(ForeignKey("users.id"))
    level: Mapped[str] = mapped_column(String(20), default="INFO", nullable=False)
    event_type: Mapped[str] = mapped_column(String(100), nullable=False)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    details: Mapped[dict | None] = mapped_column(JSON)

    project = relationship("Project", back_populates="logs")
