from fastapi import FastAPI

app = FastAPI()
from routers.authentication import router

app.include_router(router)


@app.get("/")
def read_root():
    return {"Hello": "World"}