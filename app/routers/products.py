from fastapi import APIRouter
from schemas.schemas import Product, SuccessResponse

router = APIRouter()


@router.get("", response_model=list[Product])
async def list_products():
    pass


@router.post("")
async def create_product(product: Product):
    pass


@router.get("/{id}", response_model=Product)
async def list_product(id: int):
    pass


@router.put("/{id}", response_model=SuccessResponse)
async def update_product(id: int):
    pass


@router.delete("/{id}", response_model=SuccessResponse)
async def delete_product(id: int):
    pass
