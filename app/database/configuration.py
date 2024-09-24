from sqlalchemy import create_engine,event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import engine


#datos para la conexion a BD

dataBaseName="gestordb"
userName="root"
userPassword=""
connectionPort=3306
server="localhost"

#creando la conexion
dataBaseConnection=f"mysql+mysqlconnector://{userName}:{userPassword}@{server}:{connectionPort}/{dataBaseName}"

#creoel motor de coneccion
engine=create_engine(dataBaseConnection)

#abrir la secion con la bd
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)
