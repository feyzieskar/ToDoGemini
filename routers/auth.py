from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Authentications"],)

@router.get("/get_user")
async def get_user():
    return "Hello World!"