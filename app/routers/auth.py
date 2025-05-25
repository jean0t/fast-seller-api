from fastapi import APIRouter
from schemas.schemas import TokenResponse

router = APIRouter()


@router.post("/login", response_model=TokenResponse)
async def login():
    pass


@router.post("/register", response_model=TokenResponse)
async def register():
    pass


@router.post("/refresh-token", response_model=TokenResponse)
async def refresh_token():
    pass
