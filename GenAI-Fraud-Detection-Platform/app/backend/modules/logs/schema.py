from app.backend.common.schemas import TimestampedResponse


class LogResponse(TimestampedResponse):
    project_id: str | None
    user_id: str | None
    level: str
    event_type: str
    message: str
    details: dict | None
