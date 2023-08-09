#dependencia de flask
from flask import Flask, render_template

#dependencia de modelos
from flask_sqlalchemy import SQLAlchemy

#dependencia de las migraciones
from flask_migrate import Migrate

#dependencia para fecha y hora
from datetime import datetime

#Dependencia para crear un formulario 
from flask_wtf import FlaskForm 

#Dependencia para añadir campos 
from wtforms import StringField, SubmitField 

#crear el objeto flask
app = Flask(__name__)

#definir 'cadena de conexion'(connectionString)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:@localhost/flask-shopy-2687340'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
app.config['SECRET_KEY'] = 'PGLO_MANITO'

#crear el objeto de modelos:
db =SQLAlchemy(app)

#crear el obejeto de migracion 
migrate=Migrate(app,db)

#Crear formulario de registro de productos 
class ProductosForm(FlaskForm):
    nombre = StringField ('Ingrese nombre del producto')
    precio = StringField ('Ingrese precio del producto')
    boton = SubmitField('REGISTRAR PRODUCTO')

#crear los modelos 
class Cliente(db.Model):
    #definir los atributos
    __tablename__="clientes"
    id=db.Column(db.Integer, primary_key = True )
    username = db.Column(db.String(120),nullable = True)
    password = db.Column(db.String(128),nullable = True)
    email = db.Column(db.String(100),nullable = True)
    #Establecer relaciones SQLAlchemy 
    ventas =  db.relationship('Venta' , backref = "cliente" , lazy = "dynamic" )
    
#crear los modelos 
class Producto(db.Model):
    #definir los atributos
    __tablename__="productos"
    id = db.Column(db.Integer, primary_key = True )
    nombre = db.Column(db.String(120))
    precio = db.Column(db.Numeric(precision = 10, scale = 2))
    imagen = db.Column(db.String(200))
    
class Venta (db.Model):
    __tablename__="ventas"
    id = db.Column(db.Integer, primary_key = True )
    fecha = db.Column(db.DateTime, default = datetime.utcnow )
    
    #clave foranea
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    #Establecer relaciones SQLAlchemy 
     

    
class Detalle (db.Model):
    __tablename__="detalles"
    id = db.Column(db.Integer, primary_key = True )
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'))
    venta_id = db.Column(db.Integer, db.ForeignKey('ventas.id'))
    cantidad = db.Column(db.Integer )
    
#Rutas 
@app.route('/productos',methods = ['GET ', 'POST'])
def nuevo_producto():
    form = ProductosForm()
    if form.validate_on_submit():
        #Crear instancia de registro de un nuevo producto
        p = Producto(nombre = form.nombre.data , precio= form.precio.data )
        #Se prepara el dato para registrarse
        db.session.add(p)
        #Se confirma la insercion a la base de datos 
        db.session.commit()
        return "Se registro correctamente"
    return render_template('nuevo_producto.html', form = form)