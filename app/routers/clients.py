from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_clients():
    pass


@router.post("/")
async def create_client():
    pass


@router.get("/{id}")
async def list_client(id: int):
    pass


@router.put("/{id}")
async def update_client(id: int):
    pass


@router.delete("/{id}")
async def delete_client(id: int):
    pass
