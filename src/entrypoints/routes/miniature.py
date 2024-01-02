from dataclasses import asdict

from fastapi import APIRouter

from domain.groups.create_miniature import create_miniature_group

miniature_router = APIRouter()

@miniature_router.get('/miniature/create')
def create_miniature_route():
    return create_miniature_group()
