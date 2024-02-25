from fastapi import Request, Body, status, HTTPException
from app.center.models import Center
from bson import ObjectId


def get_collection_centers(request: Request):
    return request.app.db["centers"]

def create_center(request: Request, center: Center = Body(...)):
    center = dict(center)
    new_center = get_collection_centers(request).insert_one(center)
    created_center = get_collection_centers(request).find_one({"_id": new_center.inserted_id})
    return created_center
                  

def list_centers(request: Request, limit: int):
    centers = get_collection_centers(request).find(limit=limit)
    return [{"id": str(center["_id"]), **center} for center in centers]


def get_center(request: Request, id: str):
    if (center := get_collection_centers(request).find_one({"_id": ObjectId(id)})):
        return {"id": str(center["_id"]), **center}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Centro Médico não Existe")


def update_center(request: Request, id: str, center: Center = Body(...)):
    center = dict(center)
    _ = get_collection_centers(request).update_one({"_id": ObjectId(id)}, {"$set": center})    
    if (center := get_collection_centers(request).find_one({"_id": ObjectId(id)})):
        return {"id": str(center["_id"]), **center}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Centro Médico não Existe")


def delete_center(request: Request, id: str):
    deleted_center = get_collection_centers(request).delete_one({"_id": ObjectId(id)})
    if deleted_center.deleted_count == 1:
        return
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Centro Médico não Existe")

