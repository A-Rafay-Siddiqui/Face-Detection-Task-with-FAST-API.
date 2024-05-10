from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.security import APIKeyHeader
from database import SessionLocal
from CRUD import create_user, get_user_by_id, update_user_name, search_users_by_name
from MachineLearning import process_image
from typing import List
import os

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Welcome to Face detection"}

# Secret key for authorization
SECRET_KEY = "BLEEDAI-Rafay-KEY"
API_KEY_HEADER = APIKeyHeader(name="Authorization")

# Authorization function
def authorize(api_key: str = Depends(API_KEY_HEADER)):
    if api_key != SECRET_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return True

# CRUD Endpoints
@app.post("/users/", response_model=None)
def create_user_endpoint(name: str, db: SessionLocal = Depends(get_db), authorized: bool = Depends(authorize)):
    return create_user(name, db)

@app.get("/users/{user_id}/name/", response_model=str)
def retrieve_user_name_by_id(user_id: int, db: SessionLocal = Depends(get_db), authorized: bool = Depends(authorize)):
    user = get_user_by_id(user_id, db)
    if user:
        return user.name
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}/name/", response_model=None)
def update_user_name_by_id(user_id: int, new_name: str, db: SessionLocal = Depends(get_db), authorized: bool = Depends(authorize)):
    user = update_user_name(user_id, new_name, db)
    if user:
        return "User name updated!"
    else:
        raise HTTPException(status_code=404, detail="User not found")

# Search Functionality
@app.get("/users/search/", response_model=List[str])
def search_users_by_name_endpoint(name: str, db: SessionLocal = Depends(get_db), authorized: bool = Depends(authorize)):
    return search_users_by_name(name, db)

# Image Processing Endpoint
@app.post("/process-image/")
async def process_uploaded_image(file: UploadFile = File(...)):
        try:
            with open(file.filename, "wb") as buffer:
                buffer.write(await file.read())

            cropped_face, face_landmarks = process_image(file.filename)
            

            os.remove(file.filename)
            if cropped_face is not None and face_landmarks is not None:   
                return "Face DETECTED."
            else:
                return "FACE NOT DETECTED."
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))