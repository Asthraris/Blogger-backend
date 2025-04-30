from fastapi import APIRouter ,Depends ,status ,HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..hashing import Hash
from .. import schema , model 

router = APIRouter( tags =["Users"])

@router.post("/signin")
def Sign_in(request :schema.User , db :Session = Depends(get_db)):
    #iske aage ka login that password must be 8 didgit woh sab frontent wale karte hai /by using react components
    #creating an model user from request user
    new_user = model.User(username =request.username , password = Hash.bcrypt(request.password)) 
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"detail" :"Successfully Signed-in"}
