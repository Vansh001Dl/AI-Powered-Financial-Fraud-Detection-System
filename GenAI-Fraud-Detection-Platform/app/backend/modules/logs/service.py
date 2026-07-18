from sqlalchemy.orm import Session

from app.backend.db.enterprise_models import AppLog
from app.backend.modules.logs.repository import LogRepository
from app.backend.modules.logs.validation import normalize_log_level


class LogService:
    def __init__(self, session: Session) -> None:
        self.session = session
        self.repository = LogRepository(session)

    def record(
        self,
        event_type: str,
        message: str,
        *,
        project_id: str | None = None,
        user_id: str | None = None,
        level: str = "INFO",
        details: dict | None = None,
    ) -> AppLog:
        log_entry = AppLog(
            project_id=project_id,
            user_id=user_id,
            level=normalize_log_level(level),
            event_type=event_type,
            message=message,
            details=details,
        )
        created = self.repository.add(log_entry)
        self.session.commit()
        return created

    def list_project_logs(self, project_id: str) -> list[AppLog]:
        return self.repository.list_for_project(project_id)
