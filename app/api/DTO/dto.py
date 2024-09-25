from pydantic import BaseModel, field
from datetime import date


#los dto son claese que establesen
#  el modelo de transferencia de datos
class usuarioDTOPeticion(BaseModel):
    nombres:str
    fechaNcimiento:date
    ubicaciom:str
    metaAhorro:float
    class config:
        orm_mode=True

class usuarioDTORespuesta(BaseModel):
    id:int
    nombres:str
    metaAhorro:float
    class config:
        orm_mode=True

class GastosDTOPeticion(BaseModel):
    categoria:str
    cantidaAhorro:float
    fechaInicioAhorro:date
    echaFinalAhorro:date
    class config:
        orm_mode=True


class GastosDTORespuesta(BaseModel):
    id:int
    cantidaAhorro:float
class config:
        orm_mode=True



class categoriaDTOPeticion(BaseModel):
     
     nombre:str
     descripcion:str
class config:
        orm_mode=True
 
class categoriaDTORespuesta(BaseModel):
     id:int
     nombre:str
     descripcion:str
class config:
        orm_mode=True


class ingrsosDTOPeticion(BaseModel):  
    valor:int
    descripcion:str
    fecha:date
class config:
        orm_mode=True
     

class ingresoDTORespuesta(BaseModel):  
    id:int 
    valor:int
    descripcion:str 
    class config:
        orm_mode=True  