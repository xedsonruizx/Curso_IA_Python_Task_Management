from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import os
from datetime import datetime

app = Flask(__name__)

# Configuración básica
app.config['SECRET_KEY'] = 'tu-clave-secreta-aqui'

# Lista en memoria para almacenar tareas (solo durante la ejecución)
tareas = []
contador_id = 1

@app.route('/')
def index():
    """Página principal - Redirige a tareas"""
    return redirect(url_for('mostrar_tareas'))

@app.route('/tareas')
def mostrar_tareas():
    """Página principal de tareas"""
    return render_template('tareas.html', lista_tareas=tareas)

@app.route('/about')
def about():
    """Página sobre nosotros"""
    return render_template('about.html')

@app.route('/api/data')
def api_data():
    """API endpoint de ejemplo"""
    data = {
        'message': 'Hola desde Flask!',
        'status': 'success',
        'data': [1, 2, 3, 4, 5]
    }
    return jsonify(data)

@app.route('/agregar', methods=['POST'])
def agregar_tarea():
    """Procesar formulario de nueva tarea"""
    global contador_id
    
    texto = request.form.get('texto', '').strip()
    
    if not texto:
        flash('El texto de la tarea no puede estar vacío', 'error')
        return redirect(url_for('tareas'))
    
    nueva_tarea = {
        'id': contador_id,
        'texto': texto,
        'hecho': False,
        'fecha_creacion': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    tareas.append(nueva_tarea)
    contador_id += 1
    
    flash(f'Tarea "{texto}" agregada correctamente', 'success')
    return redirect(url_for('mostrar_tareas'))

@app.route('/completar/<int:tarea_id>')
def completar_tarea(tarea_id):
    """Marcar una tarea como completada"""
    global tareas
    
    for tarea in tareas:
        if tarea['id'] == tarea_id:
            tarea['hecho'] = True
            tarea['fecha_completado'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            flash(f'Tarea "{tarea["texto"]}" marcada como completada', 'success')
            break
    else:
        flash('Tarea no encontrada', 'error')
    
    return redirect(url_for('mostrar_tareas'))

@app.route('/eliminar/<int:tarea_id>')
def eliminar_tarea(tarea_id):
    """Eliminar una tarea"""
    global tareas
    
    for i, tarea in enumerate(tareas):
        if tarea['id'] == tarea_id:
            texto_tarea = tarea['texto']
            del tareas[i]
            flash(f'Tarea "{texto_tarea}" eliminada', 'success')
            break
    else:
        flash('Tarea no encontrada', 'error')
    
    return redirect(url_for('mostrar_tareas'))

@app.route('/editar/<int:tarea_id>')
def editar_tarea(tarea_id):
    """Mostrar formulario de edición"""
    global tareas
    
    for tarea in tareas:
        if tarea['id'] == tarea_id:
            if tarea['hecho']:
                flash('No se puede editar una tarea completada', 'error')
                return redirect(url_for('mostrar_tareas'))
            return render_template('editar_tarea.html', tarea=tarea)
    
    flash('Tarea no encontrada', 'error')
    return redirect(url_for('mostrar_tareas'))

@app.route('/actualizar/<int:tarea_id>', methods=['POST'])
def actualizar_tarea(tarea_id):
    """Actualizar el texto de una tarea"""
    global tareas
    
    nuevo_texto = request.form.get('texto', '').strip()
    
    if not nuevo_texto:
        flash('El texto de la tarea no puede estar vacío', 'error')
        return redirect(url_for('editar_tarea', tarea_id=tarea_id))
    
    for tarea in tareas:
        if tarea['id'] == tarea_id:
            if tarea['hecho']:
                flash('No se puede editar una tarea completada', 'error')
                return redirect(url_for('mostrar_tareas'))
            
            texto_anterior = tarea['texto']
            tarea['texto'] = nuevo_texto
            tarea['fecha_modificacion'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            flash(f'Tarea actualizada: "{texto_anterior}" → "{nuevo_texto}"', 'success')
            break
    else:
        flash('Tarea no encontrada', 'error')
    
    return redirect(url_for('mostrar_tareas'))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Página de contacto con formulario"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Aquí procesarías el formulario
        return render_template('contact.html', 
                             success=True, 
                             name=name)
    
    return render_template('contact.html')

@app.errorhandler(404)
def not_found(error):
    """Manejo de errores 404"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Manejo de errores 500"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Configuración para desarrollo
    debug_mode = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    port = int(os.environ.get('PORT', 5000))
    
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
