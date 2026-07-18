def normalize_log_level(level: str) -> str:
    return level.upper().strip() or "INFO"
