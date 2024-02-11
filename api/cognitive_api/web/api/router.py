from fastapi.routing import APIRouter

from cognitive_api.web.api import monitoring

api_router = APIRouter()
api_router.include_router(monitoring.router)
