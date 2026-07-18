from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.backend.api.deps import get_current_user
from app.backend.db.session import get_db_session
from app.backend.modules.logs.schema import LogResponse
from app.backend.modules.logs.service import LogService

router = APIRouter(prefix="/logs", tags=["logs"])


@router.get("/projects/{project_id}", response_model=list[LogResponse])
def list_logs(
    project_id: str,
    _: object = Depends(get_current_user),
    session: Session = Depends(get_db_session),
) -> list[LogResponse]:
    service = LogService(session)
    return [LogResponse.model_validate(item) for item in service.list_project_logs(project_id)]
