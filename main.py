# main.py
from fastapi import FastAPI
from routes.camera_routes import router as camera_router

app = FastAPI()

# Include the routes from camera_routes.py
app.include_router(camera_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)