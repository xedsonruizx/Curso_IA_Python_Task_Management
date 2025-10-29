# Instrucciones para ejecutar la aplicación Flask

## Instalación

1. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución

2. Ejecuta la aplicación:
```bash
python app.py
```

3. Abre tu navegador en: http://localhost:5000

## Estructura del proyecto

```
Curso_Python_IA2/
├── app.py              # Aplicación principal Flask
├── requirements.txt    # Dependencias
├── templates/          # Templates HTML
│   ├── base.html      # Template base
│   ├── index.html     # Página principal
│   ├── about.html     # Página acerca de
│   ├── contact.html   # Página de contacto
│   ├── 404.html       # Error 404
│   └── 500.html       # Error 500
└── static/            # Archivos estáticos
    ├── css/
    │   └── style.css  # Estilos CSS
    └── js/
        └── main.js    # JavaScript
```

## Características incluidas

- ✅ Rutas básicas (/, /about, /contact)
- ✅ API endpoint (/api/data)
- ✅ Manejo de formularios
- ✅ Manejo de errores (404, 500)
- ✅ Templates con Jinja2
- ✅ Estilos CSS responsivos
- ✅ JavaScript interactivo
- ✅ Navegación entre páginas

## Personalización

Puedes modificar:
- Colores en `static/css/style.css`
- Funcionalidad en `static/js/main.js`
- Contenido en los templates HTML
- Rutas en `app.py`
