from fastapi import APIRouter, FastAPI

shorten_router = APIRouter(prefix="/api/v1/shorten", tags=["shorten"])

@shorten_router.get("/")
def hello():
    return {
        "message": "Success"
    }


def include_shorten_routes(app: FastAPI):
    app.include_router(shorten_router)
