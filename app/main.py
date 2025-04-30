from fastapi import FastAPI
#sessio is an instance of db we get per resquest operation in http
from . import model
from .database import engine
from dotenv import load_dotenv
from .routers import user,blog , authentication

app = FastAPI()
# loads the.env file file
load_dotenv()

model.Base.metadata.create_all(engine)

@app.get("/")
def greet():
    return "hello"

app.include_router(user.router)
app.include_router(blog.router)
app.include_router(authentication.router)






