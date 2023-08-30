#Dependencia para hacer un blueprint/paquete
from flask import Blueprint

#Definir paquete de productos
index_blueprint = Blueprint ('index_blueprint', __name__, url_prefix ='/index', template_folder = 'templates')

from . import routes