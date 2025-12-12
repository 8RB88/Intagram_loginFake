import json
import os
from flask import Flask, request, redirect, url_for

# 1. Configuración de la aplicación y el archivo JSON
app = Flask(__name__)
USERS_FILE = 'users.json'

def load_users():
    """Carga los usuarios existentes del archivo JSON o devuelve una lista vacía si no existe."""
    if not os.path.exists(USERS_FILE) or os.stat(USERS_FILE).st_size == 0:
        return []
    try:
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Esto ocurre si el archivo existe pero no tiene un formato JSON válido (e.g., está vacío)
        return []
    except Exception as e:
        print(f"Error al cargar usuarios: {e}")
        return []

def save_users(users):
    """Guarda la lista completa de usuarios en el archivo JSON."""
    try:
        with open(USERS_FILE, 'w') as f:
            json.dump(users, f, indent=4) # 'indent=4' para que el JSON sea fácil de leer
    except Exception as e:
        print(f"Error al guardar usuarios: {e}")

# 2. Rutas del servidor
@app.route('/')
def index():
    """Ruta para servir la página principal (index.html)."""
    # Usaremos una simple respuesta de texto ya que no estamos sirviendo el HTML desde Flask en este ejemplo simple.
    # En un entorno real, usarías 'return render_template('index.html')'
    return redirect(url_for('static', filename='index.html')) # Nota: Flask intenta servir archivos estáticos, para la prueba
                                                             # es mejor abrir index.html directamente en el navegador.

@app.route('/register', methods=['POST'])
def register():
    """Recibe los datos del formulario y los guarda en el JSON."""
    # 1. Obtener datos del formulario
    email = request.form.get('email')
    password = request.form.get('password') 

    if not email or not password:
        return "Faltan datos de correo o contraseña.", 400

    # 2. Cargar usuarios existentes
    users = load_users()

    # 3. Crear el nuevo registro
    # ¡ADVERTENCIA DE SEGURIDAD! NUNCA guardes contraseñas en texto plano en un sistema real. 
    # Siempre debes usar una función de hash (como bcrypt).
    new_user = {
        'email': email,
        'password': password 
    }

    # 4. Agregar el nuevo usuario y guardar
    users.append(new_user)
    save_users(users)

    # 5. Responder al usuario - Redirigir a una página de éxito
    # En este caso, volvemos a abrir el archivo index.html
    print(f"Nuevo usuario registrado: {email}")
    return "<h1>¡Registro exitoso!</h1><p>Usted a sido engañado con exito</p><a href='/'>Volver</a>", 201

# 3. Ejecutar la aplicación
if __name__ == '__main__':
    print("Servidor Flask inicializado. Para usarlo, abre tu archivo index.html modificado en el navegador.")
    print("Para iniciar el servidor, abre la terminal en esta carpeta y ejecuta:")
    print("python app.py")
    # Para pruebas, el servidor se ejecuta en http://127.0.0.1:5000/
    app.run(debug=True)