from fastapi import FastAPI, status
from pydantic import BaseModel, validator, ValidationError


app=FastAPI()


a = []
symbol = [
    '!', '"', '#', '$', '%',
    '&', "'", '(', ')', '*', 
    '+', ',', '-', '.', '/', 
    ':', ';', '<', '=', '>', 
    '?', '@', '[',  ']', '^', 
    '_', '`', '{', '|', '}', '~'
    ]


class User(BaseModel):
    first_name:str
    second_name:str
    email:str
    password:str
    phone:str


    @validator('first_name')
    def first_name(cls, v):
        if not str(v).isalpha():
            return ValueError("Firstname must include only letters")
        return v

    @validator('second_name')
    def second_name(cls, v):
        if not str(v).isalpha():
            return ValueError("Secondname must include only letters")
        return v

    @validator('email')
    def email(cls, v):
        if "@gmail.com" or "@ukr.net" not in v:
            raise ValueError("Email must include: @gmail.com or @ukr.net ")
        return v
    
    @validator('password')
    def password(cls, v):
        if len(v)>8:
            for x in symbol:
                if x not in v:
                    return ValueError("Password must include one special symbol")
        elif len(v)<8:
            return ValueError("Password must have 8 symbols")
        return v
    
    @validator('phone')
    def phone(cls, v):
        if "+380" not in v:
            return ValueError("Number must start from: +380")
        return v


@app.get("/users/")
async def users():
    return a


@app.post("/users/")
async def create_user(user:User):
    for user in a:
        if user:
            a.append(user)
    return a