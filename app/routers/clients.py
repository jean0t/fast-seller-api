from fastapi import APIRouter
from schemas.schemas import Client, ClientRegister, SuccessResponse

router = APIRouter()


@router.get("", response_model=list[Client])
async def list_clients():
    pass


@router.post("", response_model=SuccessResponse)
async def create_client(client: ClientRegister):
    pass


@router.get("/{id}", response_model=Client)
async def list_client(id: int):
    pass


@router.put("/{id}", response_model=SuccessResponse)
async def update_client(id: int):
    pass


@router.delete("/{id}", response_model=SuccessResponse)
async def delete_client(id: int):
    pass
