# User-Crud-operation-Using-FastApi-
Created a Simple crud operation using Fastapi Framework) with Api key Authentication.

## Overview
This project is a FastAPI-based API for performing CRUD operations on a User model. It includes functionalities such as user creation, retrieval, updating, and deletion, along with API key authentication for secure access.

## Project Structure
app---->(folder)
- **crud.py:** The main FastAPI application file.
- **database.py:** Database configuration and session handling.
- **models.py:** SQLAlchemy models for the User and APIKey entities.
- **schemas.py:** Pydantic models for request and response data.
- **requirements.txt:** Dependency list for the project.

  ### Installation

1. Clone the repository:
    git clone https://github.com/

2. Navigate to the project directory:
    cd Assignment/app
   
3. Create the python virtual environment.
    python -m venv env

4. Install dependencies:
    pip install -r requirements.txt

### Running the Application
python crud.py


The API will be available at http://127.0.0.1:8000

## API Endpoints
POST /generate-api-key: Generate a new API key for authentication.
POST /create: Create a new user profile.
GET /get/{id}: Retrieve a user's profile by ID.
PUT /update/{id}: Update a user's profile by ID.
DELETE /delete/{id}: Delete a user's profile by ID.

## Documentation
API documentation is available at http://127.0.0.1:8000/docs(here in this url will get a swagger docs) and http://127.0.0.1:8000/redoc(here in this url will get a Redoc docs).
