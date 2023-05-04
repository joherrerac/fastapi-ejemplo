from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.user import userEntity, usersEntity
from models.user import User
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()

@user.get('/users', response_model=list[User], tags=["users"])
def find_all_user():
    return usersEntity(conn.local.user.find())

@user.post("/users", response_model=User, tags=["users"])
def create_user(user: User):
    new_user = dict(user)
    #del new_user[id]
    
    #id = conn.local.user.insert_one(new_user).inserted_id
    #conn.local.user.find_one({"_id":id})
    
    print(new_user)
    return "received"

@user.get('/users/{id}', response_model=User, tags=["users"])
def find_user(id: int):
    print(id)
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))
    return "received"

@user.put('/users/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
def update_user(id: int, user: User):
    conn.local.user.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))

@user.delete('/users/{id}', response_model=User, tags=["users"])
def delete_user(id: int):
    userEntity(conn.local.user.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)