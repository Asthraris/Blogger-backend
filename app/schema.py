from pydantic import BaseModel

class baseUser(BaseModel):
    usid:int
    username: str
    password: str 

class User(BaseModel):
    username: str
    password: str

class showUser(BaseModel):
    username: str

    class Config:
        from_attributes = True

class Blog(BaseModel):
    title: str
    body: str

class showBlog(BaseModel):
    title: str
    body: str
    creator: showUser  # expects relationship in ORM

    class Config:
        from_attributes = True



class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    usid: int | None = None
