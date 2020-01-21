from flask import Flask, url_for, session, request, redirect, render_template
#* Importación Paquete con la clase
from paquete.Clase import nombreClase
#*Random
import random
#* CSV
import csv
# *Importar MONGO DB
from pymongo import MongoClient

# *DATOS BASE DE DATOS EN LA NUBE
'''
usuario: mongodb
contraseña:mongodb
'''

# * Intanciar Flask
app = Flask(__name__)

# * Crear un llave/clave secreta para SESSION
app.config['SECRET_KEY'] = 'SUPER SECRETO'


# **************************************
# * ULR Conexion
MONGO_URL_ATLAS = 'mongodb+srv://mongodb:mongodb@cluster0-l6v7e.mongodb.net/test?retryWrites=true&w=majority'

# * Establecer conexion
client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs=False)

# * Creacion base de datos MongoDB
db = client['nombre_BD']

# * Creacion coleccion
collection = db['nombreCollection']

#* Collecion usuarios, por si necesitas un login
# collectionUsuarios = db['usuarios']

#*******************************************

#* Objeto
# objetoClase = nombreClase()


#*******************************************

# * Coleccion con la información de la Inmobiliaría

# ******************************************
#* RUTE REDIRECCIONAR
@app.route('/')
def redireccionar():

    return redirect(url_for('home'))

# ******************************************
#* RUTE HOMRE
@app.route('/home')
def home():

    return render_template('home.html')

# ******************************************
#* Si tienes SESSION, que cuando vuelva a HOME, toda la sección que tengas se borre, en este
#* caso es con POST, es decir, que según la página en la que estes, el boton para volver a home.html
# #* debe tener un FORM de POST.
#* Por sí lo necesitas
# @app.route('/home', methods=['GET', 'POST'])
# def homeDatos():

#     if request.method == 'POST':

#         session.clear()

#     if 'usuario' in session:

#         return redirect(url_for('nuevaRuta'))

#     return render_template('home.html')

#************************************************

#* Login por si lo necesitas
#* Solo le falta la contraseña, simplemente sería agregarsela
# @app.route('/usuario')
# def usuario():

#     return render_template('usuario.html')

# ******************************************
# @app.route('/usuario', methods=['POST'])
# def usuariodatos():

#     # * Lista que almacena al usuario
#     listaUsuarioCorrecto = []

#     usuario = request.form['usuario']

#     leer_usuario = collectionUsuarios.find({'usuario': f'{usuario}'})

#     # print(list(leer_usuario))

#     for i in leer_usuario:

#         print(i['usuario'])
#         listaUsuarioCorrecto.append(i['usuario'])

#     # print(listaUsuarioCorrecto[0])

#     if listaUsuarioCorrecto != []:

#         if listaUsuarioCorrecto[0] == usuario:
#             # * iniciar sesion
#             # * Limpiamos la session cada vez que haga una nueva session.
#             session.clear()
#             session['usuario'] = usuario
#             print('session creada')

#             return redirect(url_for('tipoDados'))

#         else:

#             return render_template('usuario.html', no_usuario=True)
#     else:

#         return render_template('usuario.html', no_usuario=True)

#     return render_template('usuario.html')


# ******************************************
# @app.route('/registro')
# def registro():

#     return render_template('registro.html')


# ******************************************
# @app.route('/registro', methods=['GET', 'POST'])
# def registroDatos():

#     if request.method == 'POST':

#         usuario = request.form['usuario']

#         leer_usuario = collectionUsuarios.find({'usuario': f'{usuario}'})

#         # print(list(leer_usuario))

#         # * Si en la BD no esta vacio, entonces el email que se ingreso en el input existe en la BD
#         if list(leer_usuario) != []:

#             return render_template('registro.html', usuario_existe=True)

#         collectionUsuarios.insert_one({"usuario": usuario})

#         return redirect(url_for('usuario'))

#     return render_template('registro.html')


# ******************************************

#* Si necesitas más rutas, copia y pega estas dos plantillas de rutas

# @app.route('/nuevaRuta')
# def nuevaRuta():

#     return render_template('nuevaRuta.html')


# ******************************************


# @app.route('/nuevaRuta', methods=['POST'])
# def nuevaRutaDatos():

# return render_template('nuevaRuta.html')

# ******************************************
#*PAGE ERROR
@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'


# ******************************************
#*MAIN
if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)