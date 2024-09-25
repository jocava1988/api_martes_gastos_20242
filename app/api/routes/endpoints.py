from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi import Depends

from app.api.DTO.dto import usuarioDTOPeticion, usuarioDTORespuesta
from app.api.models.tablasSQL import Usuario
from app.database.configuration import SessionLocal, engine

rutas=APIRouter()

def conectarConBd():
    try:
        baseDtos=SessionLocal() 
        yield baseDtos
    except Exception as error:
        baseDtos.rollback()
        raise error

    finally:
        baseDtos.close()