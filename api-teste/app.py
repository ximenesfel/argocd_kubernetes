from fastapi import FastAPI, APIRouter 

router = APIRouter(
    prefix='/saf',
    tags = ['addition']
)

@router.get("/ping")
def pong():
    """
    Sanity check - this will let the user know that the service is operational.

    It is also used as part of the HEALTHCHECK. Docker uses curl to check that the API service is still running, by exercising this endpoint.

    """
    return {"ping": "pong!"}

app = FastAPI()

app.include_router(router)