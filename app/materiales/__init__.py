#Dependencia para hacer un blueprint/paquete
from flask import Blueprint

#Definir paquete de productos
materiales = Blueprint ('materiales', __name__, url_prefix ='/materiales', template_folder = 'templates')

from . import routes