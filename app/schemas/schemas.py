from pydantic import BaseModel, EmailStr, SecretStr
from datetime import datetime


#===================================| Client models

class Client(BaseModel):
    id: int|None = None
    cpf: str
    name: str
    email: EmailStr
    role: str = "client"


class ClientRegister(BaseModel):
    cpf: str = Field(pattern=r'^\d{11}$')
    name: str
    password: SecretStr
    email: EmailStr
    role: str = "client"



#===================================| Product models

class Product(BaseModel):
    name: str
    description: str
    price: float
    section: str
    bar_code: str
    quantity: int
    expiration_date: datetime|None = None
    images: list[bytes]
    available: bool


#===================================| Order models

class OrderResponse(BaseModel):
    id: int
    name: str
    products: list[Product]
    status: str
    client: Client


#===================================| Authentication model

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    refresh_token: str|None = None
    expires_in: str|None = None


#===================================| Status Response

class SuccessResponse(BaseModel):
    status: bool
    message: str|None = None
