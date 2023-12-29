from fastapi import FastAPI

from entrypoints.routes.miniature import create_miniature_route

app = FastAPI()

app.include_router(create_miniature_route)