from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="REST API with mongo DB",
    description="wena po",
)

app.include_router(user)