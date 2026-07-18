from sqlalchemy import desc, select

from app.backend.common.repository import BaseRepository
from app.backend.db.enterprise_models import AppLog


class LogRepository(BaseRepository[AppLog]):
    model = AppLog

    def list_for_project(self, project_id: str) -> list[AppLog]:
        stmt = select(AppLog).where(AppLog.project_id == project_id).order_by(desc(AppLog.created_at))
        return list(self.session.scalars(stmt))
