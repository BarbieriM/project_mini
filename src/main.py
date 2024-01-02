from fastapi import FastAPI

from entrypoints.routes.miniature import miniature_router

app = FastAPI()

app.include_router(miniature_router)