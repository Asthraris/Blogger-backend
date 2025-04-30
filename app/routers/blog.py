from fastapi import APIRouter , status , HTTPException ,Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import  model ,schema
from typing import List

from ..oauth2 import get_current_user
router = APIRouter(prefix="/blog" , tags=["Blogs"])

@router.post("", status_code=status.HTTP_201_CREATED)
def create_blog(
    request: schema.Blog,
    db: Session = Depends(get_db),
    curr_user: schema.baseUser = Depends(get_current_user)
):
    new_blog = model.Blog(
        title=request.title,
        body=request.body,
        user_id=curr_user.usid  # Use user_id for FK
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {"detail": "Created", "blog_id": new_blog.id}



@router.get("/all",status_code= status.HTTP_200_OK , response_model= List[schema.showBlog])
def response(db: Session = Depends(get_db), curr_user: model.User = Depends(get_current_user)):
    blogs = db.query(model.Blog).filter(model.Blog.user_id == curr_user.usid).all()
    return blogs

@router.get("/{id}" , status_code= status.HTTP_200_OK , response_model= schema.showBlog)
def response(id :int, db :Session = Depends(get_db), curr_user :schema.showUser =Depends(get_current_user)):
    blog = db.query(model.Blog).filter(model.Blog.user_id == curr_user.usid , model.Blog.id == id).first()

    if not blog :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="NOT FOUND")
        
    return blog

@router.put("/{id}", status_code=status.HTTP_200_OK)
def update(id: int, request: schema.Blog, db: Session = Depends(get_db), curr_user :schema.showUser =Depends(get_current_user)):
    blog = db.query(model.Blog).filter(model.Blog.user_id == curr_user.usid ,model.Blog.id == id).first()  # Retrieve actual instance
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")  # Correctly raise exception
    
    blog.title = request.title
    blog.body = request.body
    
    db.commit()
    return {"detail": "Updated"}



@router.delete("/{id}" , status_code= status.HTTP_200_OK)
def destroy(id :int,db:Session = Depends(get_db), curr_user :schema.showUser =Depends(get_current_user)):

    blog = db.query(model.Blog).filter(model.Blog.user_id == curr_user.usid ,model.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_204_NOT_FOUND,detail="NOT AVAILABLE")
    db.delete(blog)
    db.commit()
    
    return {"detail":"deleted"}