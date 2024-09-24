from sqlalchemy import column,Integer, String, Float, Date, ForeignKey

from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

#llamado a la base para crear tablas
Base=declarative_base()

#definicion de las tablas de mi modelo

#usuario
class Usuario(Base):
    __tablename__='Usuario'
    id=column(Integer, primary_key=True, autoincrement=True)
    nombres=column(String(50))
    fechaNacimiento=column(Date)
    ubicacion=column(String(100))
    metaAhorro=column(Float)

class Gastos(Base):
    __tablename__='Gastos'
    id=column(Integer, primary_key=True, autoincrement=True)
    categoria=column(String(100))
    cantidaAhorro=column(Float)
    fechaInicioAhorro=column(Date)
    fechaFinalAhorro=column(Date)
    

class categoria(Base):
    __tablename__='categorias'
    #id
    #nombre
    #descripcion
    #fotocategoria
    pass

class ingrsos(Base):
    __tablename__='Ingresos'
    #id
    #valor
    #descripcion
    #fecha
    pass

