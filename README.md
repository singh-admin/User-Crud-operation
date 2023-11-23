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
    git clone git@github.com:singh-admin/User-Crud-operation.git

2. Navigate to the project directory:
    cd Assignment/app
   
3. Create the python virtual environment.
    python -m venv env
   
4. Activate the virtual environment.
    env\Scripts\activate

5. Install dependencies:
    pip install -r requirements.txt

### Running the Application
    python crud.py

Notes: once will run the code (python crud.py) then auto user.db(sqllite) will create and two table will migrate into the database.

step: then visit the given url http://127.0.0.1:8000/docs will get swagger docs.
![image](https://github.com/singh-admin/User-Crud-operation-Using-FastApi-/assets/61795935/1aac38ea-7a1a-4da6-a8fc-5013dad03a5b)

      1. need to create a user first.
      ![image](https://github.com/singh-admin/User-Crud-operation/assets/61795935/21bdda42-aed2-4b32-b453-4450b95c343d)

      2. after that if you want to use the get method for that you need to pass api key (key authentication).
      ![image](https://github.com/singh-admin/User-Crud-operation-Using-FastApi-/assets/61795935/8e0e123f-cae6-42bf-9644-23b4e57fbe89)
      ![image](https://github.com/singh-admin/User-Crud-operation-Using-FastApi-/assets/61795935/7db7fd37-fc3b-47ee-aa0c-14f1faa6f537)
      3. that api key need to pass while hitting get method.
      ![image](https://github.com/singh-admin/User-Crud-operation-Using-FastApi-/assets/61795935/ec7543ef-f6e5-4dab-913e-784635e08b2f)
      ![image](https://github.com/singh-admin/User-Crud-operation-Using-FastApi-/assets/61795935/1f9e0819-087f-4103-8281-571024cb5931)


The API will be available at http://127.0.0.1:8000

## API Endpoints
POST /generate-api-key: Generate a new API key for authentication.
POST /create: Create a new user profile.
GET /get/{id}: Retrieve a user's profile by ID.
PUT /update/{id}: Update a user's profile by ID.
DELETE /delete/{id}: Delete a user's profile by ID.

## Documentation
API documentation is available at http://127.0.0.1:8000/docs(here in this url will get a swagger docs) and http://127.0.0.1:8000/redoc(here in this url will get a Redoc docs).

