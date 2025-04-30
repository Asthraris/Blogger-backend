from fastapi import APIRouter , Depends , status ,HTTPException
from sqlalchemy.orm import Session
from .. import schema , model
from ..database import get_db
from ..hashing import Hash

from ..token import ACCESS_TOKEN_EXPIRE_MINUTES , create_access_token
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(tags=["Authentication"])

@router.post("/login", status_code= status.HTTP_200_OK)
def login(request :OAuth2PasswordRequestForm  = Depends(),db :Session = Depends(get_db) ):
    user = db.query(model.User).filter(model.User.username==request.username).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND ,detail="user with this username not exists")
    if not Hash.verify(request.password,user.password):
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED ,detail="Wrong password")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)}
    )
    return schema.Token(access_token=access_token, token_type="bearer")
