from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Base de datos ficticia para almacenar usuarios y contraseñas
usuarios = {
    'usuario1': 'contraseña1',
    'usuario2': 'contraseña2'
}

@app.route('/')
def index():
    return render_template('in.html')

@app.route('/registro', methods=['POST'])
def registro():
    usuario = request.form.get('usuario')
    contrasena = request.form.get('contrasena')

    # Verificar si los datos necesarios están presentes en la solicitud
    if not usuario or not contrasena:
        return render_template('in.html', error='Faltan datos en el formulario de registro')

    # Verificar si el usuario ya existe en la base de datos
    if usuario in usuarios:
        return render_template('in.html', error='El usuario ya existe. Por favor, elige otro nombre de usuario.')

    # Guardar usuario y contraseña en la base de datos (en este caso, un diccionario)
    usuarios[usuario] = contrasena

    return render_template('in.html', mensaje='Registro exitoso. Ahora puedes iniciar sesión.')

@app.route('/inicio_sesion', methods=['POST'])
def inicio_sesion():
    usuario = request.form.get('usuario')
    contrasena = request.form.get('contrasena')

    # Verificar si los datos necesarios están presentes en la solicitud
    if not usuario or not contrasena:
        return render_template('in.html', error='Faltan datos en el formulario de inicio de sesión')

    # Verificar si el usuario y la contraseña coinciden con la base de datos
    if usuario in usuarios and usuarios[usuario] == contrasena:
        return render_template('in.html', mensaje='Autenticación satisfactoria. ¡Bienvenido, {}!'.format(usuario))
    else:
        return render_template('in.html', error='Error en la autenticación. Verifica tus credenciales e intenta de nuevo.')

if __name__ == '__main__':
    app.run(debug=True)
