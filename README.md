
# FastAPI Blog Backend with JWT Authentication

This is a backend API built with FastAPI, where users can create, read, update, and delete their own blog posts. User authentication is handled via JWT tokens to ensure that each user has access only to their blogs.

## Requirements

Make sure you have Python 3.7+ installed.

### 1. Install dependencies

Clone this repository and navigate to the project folder.

Install the required dependencies with:

```bash
pip install -r requirements.txt
```

### 2. Requirements file (`requirements.txt`)

Here is the content of the `requirements.txt`:
- `fastapi`: The web framework.
- `uvicorn`: ASGI server for running the app.
- `python-jose`: For JWT token encoding and decoding.
- `pydantic`: For data validation.
- `sqlalchemy`: ORM for handling database operations.
- `databases`: Async database support.
- `passlib`: For password hashing.
- `bcrypt`: For password algorithm.
- `dotenv`: for separate env in project.
  

## Setup Instructions

### 1. Edit `.env` file
```
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./test.db 
```
>- `SECRET_KEY`: Your secret key used for signing JWT tokens.
>- `ALGORITHM`: The algorithm used to encode and decode JWT tokens (usually `HS256`).
>- `ACCESS_TOKEN_EXPIRE_MINUTES`: Expiration time for the JWT token in minutes.
>- `DATABASE_URL`: URL to your local database (SQLite for testing in this case).



### 3. Run the FastAPI server

Use Uvicorn to run the FastAPI app locally. Run the following command:

```bash
uvicorn app.main:app --reload
```

This will start the app on `http://127.0.0.1:8000/`.

## API Endpoints
Use Swagger's UI to naviagate :`http://localhost:8000/docs`
## JWT Authentication

The app uses JWT tokens for authentication. After logging in, the user will receive a JWT token, which should be included in the `Authorization` header as `Bearer <token>` for any endpoint that requires authentication.
>so u need to create user/signin the authenticate yourself /login before using blogs endpoints

## Conclusion
just use it ...
