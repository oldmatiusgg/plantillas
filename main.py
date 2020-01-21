from flask import Flask, url_for, session, request, redirect, render_template
# * Importación Paquete con la clase
from reciclaje.Reciclaje import Reciclaje
# *Random
import random
# * CSV
import csv
# *Importar MONGO DB
from pymongo import MongoClient
# * Libreria Documentación
import doctest

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
MONGO_URL_ATLAS = 'mongodb+srv://matius:mongodb@primercluster-hewbh.mongodb.net/test?retryWrites=true&w=majority'

# * Establecer conexion
client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs=False)

# * Creacion base de datos MongoDB
db = client['ProyectoFinal_BD']

# * Creacion coleccion
collection = db['nombreCollection']

# * Collecion usuarios, por si necesitas un login
collectionUsuarios = db['usuarios']

# *******************************************

# * Objeto
# objetoClase = nombreClase()


# *******************************************

# * Coleccion con la información de la Inmobiliaría

# ******************************************
# * RUTE REDIRECCIONAR
@app.route('/')
def redireccionar():
    """
    RUTA REDIRECCIONAR A LA RUTA HOME
    """

    return redirect(url_for('home'))

# ******************************************
# * RUTE HOMRE
@app.route('/home')
def home():
    """
    RUTA HOME
    """

    logo = 'logo'
listaUsuarioCorrecto[1] == contrasenya
    # print(f'todavía existe la session: ' + session['usuario'])

    if 'usuario' in session:

        print(f'todavía existe la session: ' + session['usuario'])

        return render_template('home.html', usuario_existe=True, logo='logo')

    return render_template('home.html', logo=logo)

# ******************************************
# * Si tienes SESSION, que cuando vuelva a HOME, toda la sección que tengas se borre, en este
# * caso es con POST, es decir, que según la página en la que estes, el boton para volver a home.html
# #* debe tener un FORM de POST.
# * Por sí lo necesitas
@app.route('/home', methods=['GET', 'POST'])
def homeDatos():
    """
    LLEGADA DE DATOS A LA RUTA HOME, ESTO ES PARA PODER LIMPIAR LA SESSION CUANDO VUELVAN A HOME A TRAVEZ DE LA APLICACIÓN.
    """

    if request.method == 'POST':

        print('Se ha limpiado la session')

        session.clear()

    return render_template('home.html', usuario_existe=False, logo='logo')

# ************************************************

# * Login por si lo necesitas
# * Solo le falta la contraseña, simplemente sería agregarsela
@app.route('/usuario')
def usuario():
    """
    RUTA USUARIO, PARA INGRESAR EL LOGIN. USUARIO Y CONTRAÑESA, O SOLO USUARIO DEPENDIENDO DEL CASO
    """

    return render_template('usuario.html')

# ******************************************
@app.route('/usuario', methods=['POST'])
def usuariodatos():
    """
    LLEGADA DATOS DE USUARIO, CON LOS DATOS DEL LOGIN, PARA PODER INGRESAR A LA APLICACIÓN EN SÍ.
    """

    # * Lista que almacena al usuario
    listaUsuarioCorrecto = []

    usuario = request.form['usuario']

    contrasenya = request.form['contrasenya']

    leer_usuario = collectionUsuarios.find({'usuario': f'{usuario}', 'password': f'{contrasenya}'})

    # print(list(leer_usuario))

    for i in leer_usuario:

        print(i['usuario'])
        listaUsuarioCorrecto.extend([i['usuario'], i['password']])

    # print(listaUsuarioCorrecto[0])

    if listaUsuarioCorrecto != []:

        if listaUsuarioCorrecto[0] == usuario and listaUsuarioCorrecto[1] == contrasenya:

            print(f'contraseña ingresada: {contrasenya}')

                
            # * iniciar sesion
            # * Limpiamos la session cada vez que haga una nueva session.
            session.clear()
            session['usuario'] = usuario
            session['password'] = contrasenya
            print('session creada')

            return redirect(url_for('perfil'))


        else:

            return render_template('usuario.html', no_usuario=True)
    else:

        return render_template('usuario.html', no_usuario=True)

    return render_template('usuario.html')


# ******************************************
@app.route('/registro')
def registro():
    """
    RUTA REGISTRO, PARA REGISTRARSE EN LA APLICACIÓN
    """

    return render_template('registro.html')


# ******************************************
@app.route('/registro', methods=['GET', 'POST'])
def registroDatos():
    """
    LLEGADA DE DATOS A LA RUTA REGISTRO. PARA REGISTRAR AL USUARIO EN LA APLICACIÓN
    """

    if request.method == 'POST':

        usuario = request.form['usuario']

        contrasenya = request.form['contrasenya']

        leer_usuario = collectionUsuarios.find({'usuario': f'{usuario}'})

        # print(list(leer_usuario))

        # * Si en la BD no esta vacio, entonces el email que se ingreso en el input existe en la BD
        if list(leer_usuario) != []:

            return render_template('registro.html', usuario_existe=True)

        collectionUsuarios.insert_one({"usuario": usuario, 'password': contrasenya})

        return redirect(url_for('usuario'))

    return render_template('registro.html')


# ******************************************

# * Si necesitas más rutas, copia y pega estas dos plantillas de rutas

@app.route('/perfil')
def perfil():

    """
    RUTA NOMBRERUTA, TE PERMITE
    """

    return render_template('perfil.html')


# ******************************************


@app.route('/perfil', methods=['POST'])
def perfilDatos():

    """
    RUTA NOMBRERUTA, TE PERMITE
    """

    #* objeto de Clase Reciclaje
    objReciclaje = Reciclaje(collectionusuarios, session['usuario'], session['password'])

    return render_template('perfil.html')

# ******************************************

# * Si necesitas más rutas, copia y pega estas dos plantillas de rutas

@app.route('/reciclar')
def reciclar():

    """
    RUTA NOMBRERUTA, TE PERMITE
    """

    return render_template('reciclar.html')


# ******************************************


@app.route('/reciclar', methods=['POST'])
def reciclarDatos():

    """
    RUTA NOMBRERUTA, TE PERMITE
    """

    return render_template('reciclar.html')

# ******************************************

# * Si necesitas más rutas, copia y pega estas dos plantillas de rutas

@app.route('/eventos')
def eventos():

    """
    RUTA NOMBRERUTA, TE PERMITE
    """


    return render_template('eventos.html')


# ******************************************


@app.route('/eventos', methods=['POST'])
def eventosDatos():

    """
    RUTA NOMBRERUTA, TE PERMITE
    """

    return render_template('eventos.html')

# ******************************************

# * Si necesitas más rutas, copia y pega estas dos plantillas de rutas

@app.route('/educacion')
def educacion():

    """
    RUTA NOMBRERUTA, TE PERMITE
    """

    return render_template('educacion.html')


# ******************************************


@app.route('/educacion', methods=['POST'])
def educacionDatos():

    """
    RUTA NOMBRERUTA, TE PERMITE
    """

    return render_template('educacion.html')

# ******************************************

# * Si necesitas más rutas, copia y pega estas dos plantillas de rutas

@app.route('/crearEvento')
def crearEvento():

    """
    RUTA NOMBRERUTA, TE PERMITE
    """

    return render_template('crearEvento.html')


# ******************************************


@app.route('/crearEvento', methods=['POST'])
def crearEventoDatos():

    """
    RUTA NOMBRERUTA, TE PERMITE
    """

    return render_template('crearEvento.html')

# ******************************************

# * Si necesitas más rutas, copia y pega estas dos plantillas de rutas

@app.route('/noticias')
def noticias():

    """
    RUTA NOMBRERUTA, TE PERMITE
    """

    return render_template('noticias.html')


# ******************************************


@app.route('/noticias', methods=['POST'])
def noticiasDatos():

    """
    RUTA NOMBRERUTA, TE PERMITE
    """

    return render_template('noticias.html')

# ******************************************

# * Si necesitas más rutas, copia y pega estas dos plantillas de rutas

@app.route('/denuncia')
def denuncia():

    """
    RUTA NOMBRERUTA, TE PERMITE
    """

    return render_template('denuncia.html')


# ******************************************


@app.route('/denuncia', methods=['POST'])
def denunciaDatos():

    """
    RUTA NOMBRERUTA, TE PERMITE
    """

    return render_template('denuncia.html')

# ******************************************

# * Si necesitas más rutas, copia y pega estas dos plantillas de rutas

# @app.route('/nuevaRuta')
# def nuevaRuta():

    """
    RUTA NOMBRERUTA, TE PERMITE
    """

#     return render_template('nuevaRuta.html')


# ******************************************


# @app.route('/nuevaRuta', methods=['POST'])
# def nuevaRutaDatos():

    """
    RUTA NOMBRERUTA, TE PERMITE
    """

# return render_template('nuevaRuta.html')

# ******************************************
# *PAGE ERROR
@app.errorhandler(404)
def page_no_found(error):

    """
    RUTA DE 'PAGINA NO ENCONTRADA', POR SI ALGUIEN PONE LA RUTA DE URL MAL.
    """
    return '<h1> Pagina no encontrada, siga buscando</h1>'


# ******************************************
# *MAIN
if __name__ == "__main__":

    """
    MAIN, PARA INICIAR MAIN.PY
    """

    app.run('0.0.0.0', '5000', debug=True)
