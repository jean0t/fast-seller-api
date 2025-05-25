from fastapi import APIRouter
from schemas.schemas import OrderResponse, SuccessResponse

router = APIRouter()


@router.get("", response_model=list[OrderResponse])
async def list_orders():
    pass


@router.post("", response_model=SuccessResponse)
async def create_order():
    pass


@router.get("/{id}", response_model=OrderResponse)
async def list_order(id: int):
    pass


@router.put("/{id}", response_model=SuccessResponse)
async def update_order(id: int):
    pass


@router.delete("/{id}", response_model=SuccessResponse)
async def delete_order(id: int):
    pass
