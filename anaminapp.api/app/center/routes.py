from fastapi import APIRouter, Body, Request, status
from app.center.models import Center, CenterResponse
from app.center import controllers
from typing import List
router = APIRouter()

@router.post("/", response_model=Center, status_code=status.HTTP_201_CREATED)
async def create_center(request: Request, center: Center = Body(...)):
    return controllers.create_center(request, center)


@router.get("/", response_model=List[CenterResponse])
async def list_centers(request: Request):
    return controllers.list_centers(request, 30)


@router.get("/{center_id}", response_model=CenterResponse)
async def get_center(request: Request, center_id: str):
    return controllers.get_center(request, center_id)


@router.put("/{center_id}", response_model=CenterResponse)
async def update_center(request: Request, center_id: str, center: Center = Body(...)):
    return controllers.update_center(request, center_id, center)


@router.delete("/{center_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_center(request: Request, center_id: str):
    return controllers.delete_center(request, center_id)

