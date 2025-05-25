from pydantic import BaseModel, EmailStr
from datetime import datetime

class User(BaseModel):
    cpf: str
    name: str
    email: EmailStr
    role: str = "client"


class Order(BaseModel):
    name: str
    quantity: int


class Products(BaseModel):
    name: str
    description: str
    price: float
    section: str
    bar_code: str
    quantity: int
    expiration_date: datetime|None = None
    images: list[bytes]
    available: bool


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    refresh_token: str|None = None
    expires_in: int|None = None
