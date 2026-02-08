# backend/app/api/whisper.py

from fastapi import APIRouter, HTTPException
from app.schemas.whisper import WhisperRequest, WhisperResponse
from app.services.whisper_service import WhisperService

router = APIRouter(prefix="/whisper", tags=["whisper"])

whisper_service = WhisperService()


@router.post("/", response_model=WhisperResponse)
def whisper(request: WhisperRequest) -> WhisperResponse:
    try:
        result = whisper_service.whisper(
            problem_statement=request.problem_statement,
            user_code=request.user_code,
        )
        return WhisperResponse(hints=result)

    except ValueError as e:
        # Guard or policy violation
        raise HTTPException(status_code=400, detail=str(e))
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

    # except Exception:
    #     # Do not leak internals
    #     raise HTTPException(
    #         status_code=500,
    #         detail="Whisperer failed to generate hints",
    #     )