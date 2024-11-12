# config.py
from urllib.parse import quote_plus

# db_config.py
CONNECT = {
    "mongo": {
        "URL": "",  # Replace with your MongoDB URI
        "DATABASE": "SmartCamera",
    }
}



SCHEMA = {
    "CAMERAS": "cameras",
    "FRAMES": "frames",
    "DETECTIONS": "detections",
    "PERSONS": "persons",
    "FACE_DETECTIONS": "face_detections",
    "TRACKS": "tracks"
}

