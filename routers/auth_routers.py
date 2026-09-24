from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def authenticated():
    return {
        "message": "you access the default authentication router",
        "authenticated": False,
    }