from fastapi import FastAPI
#sessio is an instance of db we get per resquest operation in http
from . import model
from .database import engine

from .routers import user,blog , authentication

app = FastAPI()
#router -don3
#relation -don3
#login -don3
#authentication
#op behind auethenti cation

model.Base.metadata.create_all(engine)

@app.get("/")
def greet():
    return "hello"

app.include_router(user.router)
app.include_router(blog.router)
app.include_router(authentication.router)






