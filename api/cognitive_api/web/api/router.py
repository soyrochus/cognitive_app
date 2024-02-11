from fastapi.routing import APIRouter

from cognitive_api.web.api import monitoring, llm

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(llm.router)
