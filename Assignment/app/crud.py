import uuid
from fastapi import  HTTPException
from database import SessionLocal
from schemas import UserCreate, UserResponse
from fastapi import FastAPI, HTTPException, Depends, HTTPException
from fastapi.security import APIKeyQuery
from sqlalchemy.orm import Session
from models import Base, User, APIKey
from schemas import UserCreate, UserResponse, APIKeyCreate
from database import SessionLocal, engine, get_db



Base.metadata.create_all(bind=engine)
# initializing the Fastapi

app = FastAPI(title="Crud Apis",
    description="Python Assignment creating users operation using fastapi",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "Users Crud operation",
            "description": "Operations related to users",
            "externalDocs": {
                "description": "Find more info here",
                "url": "https://example.com",
            },
        },
        # Add more tags as needed
    ],)

# Define the security scheme for API key authentication using a query parameter
api_key_query = APIKeyQuery(name="api_key", auto_error=False)

# Function to generate and save a new API key for a given user name
def generate_and_save_api_key(api_key_create: APIKeyCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.name == api_key_create.name).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Generate a unique API key using uuid
    new_api_key = str(uuid.uuid4())
    
    api_key = APIKey(key=new_api_key, user_id=user.id)
    db.add(api_key)
    db.commit()
    return {"api_key": new_api_key}

def get_api_key(api_key: str = Depends(api_key_query), db: Session = Depends(get_db)):
    api_key_obj = db.query(APIKey).filter(APIKey.key == api_key).first()
    if api_key_obj is None:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return api_key

# post method used to generate the key for authentication.
@app.post("/generate-api-key", response_model=dict, tags=["Users Crud operation"])
async def generate_api_key(api_key_create: APIKeyCreate, db: Session = Depends(get_db)):
    return generate_and_save_api_key(api_key_create, db)

# post method used to create the record in user table
@app.post("/create", response_model=UserResponse, tags=["Users Crud operation"])
async def create_user(user: UserCreate):
    db_item = User(name=user.name, message=f"Welcome, {user.name} your profile got created")
    db = SessionLocal()
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    db.close()
    return db_item

# get method used to fetch the particular record from user table
@app.get("/get/{id}", response_model=UserResponse, tags=["Users Crud operation"])
async def get_user(id: int, key: UserResponse = Depends(get_api_key)):
    db = SessionLocal()
    user = db.query(User).filter(User.id == id).first()
    db.close()
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")
    user.message = f"Welcome, {user.name} !"
    return user

# put method used to update the particular record in user table
@app.put("/update/{id}", response_model=UserResponse, tags=["Users Crud operation"])
async def update_user(id: int, item: UserCreate):
    db = SessionLocal()
    user = db.query(User).filter(User.id == id).first()
    if user is None:
        db.close()
        raise HTTPException(status_code=404, detail="user not found")
    user.name = item.name
    user.message = f"Welcome, {item.name} your profile got updated"
    db.commit()
    db.refresh(db_item)
    db.close()
    return user

# Delete method used to delete the particular record from user table
@app.delete("/delete/{id}", response_model=UserResponse, tags=["Users Crud operation"])
async def delete_user(id: int, key: UserResponse = Depends(get_api_key)):
    db = SessionLocal()
    user = db.query(User).filter(User.id == id).first()
    if user is None:
        db.close()
        raise HTTPException(status_code=404, detail="user not found")
    user.message = f"Welcome, {user.name} your profile got deleted"
    db.delete(db_item)
    db.commit()
    db.close()
    return user

# Run the Application through Uvicorn.
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1")


