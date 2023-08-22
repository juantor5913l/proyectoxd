#Dependencia para hacer un blueprint/paquete
from flask import Blueprint

#Definir paquete de productos
ordenes = Blueprint ('ordenes', __name__, url_prefix ='/ordenes', template_folder = 'templates')

from . import routes