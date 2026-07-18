from typing import Any


def log_payload(event_type: str, message: str, **details: Any) -> dict[str, Any]:
    return {"event_type": event_type, "message": message, "details": details or None}
