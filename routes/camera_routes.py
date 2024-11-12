# routes/camera_routes.py
from fastapi import APIRouter, Query, HTTPException, Depends
from typing import List
import os
import sys
import asyncio

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.append(project_root)

from controllers.camera_controller import CameraController
from utils.util import validate_input, validate_positive_number

router = APIRouter()


@router.get("/cameras")
async def get_cameras(N: int = Query(description="Number of cameras to retrieve")):
    try:
        if not validate_positive_number(N):
            return {"status": False, "message": "Input must be a positive number"}
        camera_controller = CameraController()
        successed, cameras = await camera_controller.get_cameras(N)
        if successed:
            return {"status": True, "data": cameras}
        else:
            return {"status": False, "error_code": 202, "error_message": "Failed to fetch cameras from the database."}
    except Exception as err:
        return {"status": False, "error_code": 404, "error_message": str(err)}
@router.post("/cameras")
async def insert_cameras(data: List[dict]):
    try:
        for camera in data:
            if not validate_input(camera):
                return {"status": False, "message": "Input must be a dictionary"}
        
        camera_controller = CameraController()
        successed = await camera_controller.insert_cameras(data)
        if successed:
            return {"status": True}
        else:
            return {"status": False, "error_code": 202, "error_message": "Failed to update cameras."}
    except Exception as err:
        return {"status": False, "error_code": 404, "error_message": str(err)}
    
    
@router.put("/cameras")
async def update_cameras(data: List[dict]):
    try:
        camera_controller = CameraController()
        successed = await camera_controller.update_cameras(data)
        if successed:
            return {"status": True}
        else:
            return {"status": False, "error_code": 202, "error_message": "Failed to update cameras."}
    except Exception as err:
        raise HTTPException(status_code=404, detail=str(err))

@router.delete("/cameras")
async def delete_cameras(data: List[str]):
    try:
        camera_controller = CameraController()
        successed = await camera_controller.delete_cameras(data)
        if successed:
            return {"status": True}
        else:
            return {"status": False, "error_code": 202, "error_message": "Failed to delete cameras."}
    except Exception as err:
        raise HTTPException(status_code=404, detail=str(err))