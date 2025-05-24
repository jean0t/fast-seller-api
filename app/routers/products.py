from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_products():
    pass


@router.post("/")
async def create_product():
    pass


@router.get("/{id}")
async def list_product(id: int):
    pass


@router.put("/{id}")
async def update_product(id: int):
    pass


@router.delete("/{id}")
async def delete_product(id: int):
    pass
