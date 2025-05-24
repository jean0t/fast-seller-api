from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_orders():
    pass


@router.post("/")
async def create_order():
    pass


@router.get("/{id}")
async def list_order(id: int):
    pass


@router.put("/{id}")
async def update_order(id: int):
    pass


@router.delete("/{id}")
async def delete_order(id: int):
    pass
