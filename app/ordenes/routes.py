from flask import render_template
from . import ordenes

@ordenes.route('/ordenes')
def listar_ordenes():
    ordenes = OrdenServicio.query.all()
    return render_template('listar_ordenes.html', ordenes=ordenes)

# Ruta para agregar una nueva orden de servicio (CREATE)
@ordenes.route('/ordenes/agregar', methods=['GET', 'POST'])
def agregar_orden():
    if request.method == 'POST':
        fecha_orden_servicio = datetime.strptime(request.form['fecha_orden_servicio'], '%Y-%m-%d')
        usuario_id = request.form['usuario_id']
        
        orden = OrdenServicio(fecha_orden_servicio=fecha_orden_servicio, usuario_id=usuario_id)
        
        db.session.add(orden)
        db.session.commit()
        
        return redirect('/ordenes')
    
    usuarios = Usuario.query.all()
    return render_template('agregar_orden.html', usuarios=usuarios)

# Ruta para editar una orden de servicio (UPDATE)
@ordenes.route('/ordenes/editar/<int:id>', methods=['GET', 'POST'])
def editar_orden(id):
    orden = OrdenServicio.query.get(id)
    
    if request.method == 'POST':
        orden.fecha_orden_servicio = datetime.strptime(request.form['fecha_orden_servicio'], '%Y-%m-%d')
        orden.usuario_id = request.form['usuario_id']
        
        db.session.commit()
        
        return redirect('/ordenes')
    
    usuarios = Usuario.query.all()
    return render_template('editar_orden.html', orden=orden, usuarios=usuarios)

# Ruta para eliminar una orden de servicio (DELETE)
@ordenes.route('/ordenes/eliminar/<int:id>')
def eliminar_orden(id):
    orden = OrdenServicio.query.get(id)
    
    if orden:
        db.session.delete(orden)
        db.session.commit()
    
    return redirect('/ordenes')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)