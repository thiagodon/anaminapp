from fastapi import APIRouter
from app.center.routes import router as center_routes


router = APIRouter()

router.include_router(center_routes, tags=['Center'], prefix='/api/center')
