from flask import render_template
from . import materiales

#Definir rutas
@materiales.route('/materiales')
def listar_materiales():
    materiales = Material.query.all()
    return render_template('listar_materiales.html', materiales=materiales)

# Ruta para agregar un nuevo material (CREATE)
@materiales.route('/materiales/agregar', methods=['GET', 'POST'])
def agregar_material():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        cantidad_stock = request.form['cantidad_stock']
        unidad_medida = request.form['unidad_medida']
        color = request.form['color']
        material = Material(nombre_material=nombre, descripcion=descripcion, precio=precio,
                            cantidad_stock=cantidad_stock, unidad_medida=unidad_medida,color=color)
        
        db.session.add(material)
        db.session.commit()
        
        return redirect('/materiales')
    
    return render_template('agregar_material.html')

# Ruta para editar un material (UPDATE)
@materiales.route('/materiales/editar/<int:id>', methods=['GET', 'POST'])
def editar_material(id):
    material = Material.query.get(id)
    
    if request.method == 'POST':
        material.nombre_material = request.form['nombre']
        material.descripcion = request.form['descripcion']
        material.precio = request.form['precio']
        material.cantidad_stock = request.form['cantidad_stock']
        material.unidad_medida = request.form['unidad_medida']
        material.color = request.form['color']
        db.session.commit()
        
        return redirect('/materiales')
    
    return render_template('editar_material.html', material=material)

# Ruta para eliminar un material (DELETE)
@materiales.route('/materiales/eliminar/<int:id>')
def eliminar_material(id):
    material = Material.query.get(id)
    
    if material:
        db.session.delete(material)
        db.session.commit()
    
    return redirect('/materiales')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
