# controllers/camera_controller.py
import os
import sys
from typing import List, Tuple

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.append(project_root)

# controllers/camera_controller.py
from database.dba.camera_dba import CameraDBA
from database.dbo.camera_dbo import CameraDBO
from utils.util import normalize_id
from typing import List, Tuple


class CameraController:
    current_cameras = []

    def __init__(self):
        self.dba = CameraDBA()

    async def get_cameras(self, n: int) -> Tuple[bool, List[dict]]:
        try:
            result = self.dba.find_many({}, n)
            CameraController.current_cameras = result
            json_cameras = [camera.to_json() for camera in result]
            successed = True
            return successed, json_cameras
        except Exception as e:
            successed = False
            print("Exception in get_cameras:", e)
            return successed, None

    async def insert_cameras(self, cameras: List[dict]) -> bool:
        try:
            # for camera in cameras:
            #     camera["multimedia"] = normalize_id(camera["multimedia"])
            cameras = [CameraDBO(**camera) for camera in cameras]
            self.dba.insert_many(cameras)
            successed = True
            return successed
        except Exception as e:
            print("Exception in insert_cameras in controllers:", e)
            successed = False
            return successed

    async def update_cameras(self, in_cameras: List[dict]) -> bool:
        try:
            in_cameras = [CameraDBO.from_json_obj(camera) for camera in in_cameras]
            current_cameras = CameraController.current_cameras
            print("current_cameras: ", current_cameras)
            current_cameras_dict = {q.id: q for q in current_cameras}
            cameras_to_update = []

            for incoming_camera in in_cameras:
                current_camera = current_cameras_dict.get(incoming_camera.id)
                print("in: ", incoming_camera)
                print("cur:", current_camera)
                if current_camera and incoming_camera != current_camera:
                    cameras_to_update.append(incoming_camera)
            if cameras_to_update:
                self.dba.update_cameras(cameras_to_update)
            successed = True
            return successed
        except Exception as e:
            print("Exception in update_cameras:", e)
            successed = False
            return successed

    async def delete_cameras(self, ids: List[str]) -> bool:
        try:
            ids = [normalize_id(id) for id in ids]
            self.dba.transaction(self.dba.delete_cameras, ids=ids)
            successed = True
            return successed
        except Exception as e:
            print("Exception in delete_cameras:", e)
            successed = False
            return successed