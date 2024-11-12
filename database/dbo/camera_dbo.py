import os
import sys
from bson import ObjectId
from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, Dict, List, Optional

# Ensure the current directory and project root are correctly set
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from patterns.base_dbo import BaseDBO

class CameraDBO(BaseDBO):
    id: Optional[ObjectId] = Field(default=None, alias="_id")
    fps: int
    framesize: str
    detail: Optional[str] = None

    model_config = ConfigDict(arbitrary_types_allowed=True, json_encoders={ObjectId: str})

    @field_validator("id", mode="before")
    def convert_to_object_id(cls, value):
        if isinstance(value, str):
            return ObjectId(value)
        return value
    
    def validate(self):
        pass


    def validate_multimedia(id):
        # TODO: Ensure the multimedia ID exists in the database.
        return True






