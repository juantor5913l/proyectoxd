#dependencia de flask
from flask import Flask

#Dependencia de configuracion 
from .config import Config #El punto es para indicarle a python que los archivos estan en el mismo paquete

#dependencia de modelos
from flask_sqlalchemy import SQLAlchemy

#dependencia de las migraciones
from flask_migrate import Migrate


#crear el objeto flask
app = Flask(__name__)

#Configuracion del objeto flask
app.config.from_object(Config)

#crear el objeto de modelos:
db =SQLAlchemy(app)

#crear el obejeto de migracion 
migrate=Migrate(app,db)

#Importar los modelos

from .models import Cliente,Venta,Detalle,Producto
