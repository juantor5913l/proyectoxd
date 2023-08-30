from flask import redirect, render_template, request
import app
#from app.models import Material
from . import index_blueprint

#Definir rutas
@index_blueprint.route('/inicio')
def go():
    materiales = app.models.Material.query.all()
    return render_template('index.html')