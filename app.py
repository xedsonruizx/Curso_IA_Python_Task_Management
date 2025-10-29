from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Configuración básica
app.config['SECRET_KEY'] = 'tu-clave-secreta-aqui'

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

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
