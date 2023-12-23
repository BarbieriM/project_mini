from dataclasses import asdict

from fastapi import APIRouter

from domain.groups.create_miniature import create_miniature_group

miniature_router = APIRouter()

@miniature_router.create('/miniature/create/{miniature}')
def create_miniature_route( id: int, image:str, name:str, type:str, size:str,):
    miniatura = create_miniature_group(
        id , 
        image, 
        name,
        type,
        size
        )
    return miniatura
