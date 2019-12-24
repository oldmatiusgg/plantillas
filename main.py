from flask import Flask, url_for, session, request, redirect, render_template
#* Importación Paquete con la clase
from restaurante.Restaurante import Restaurante
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
db = client['examen_m4_c2']

# * Creacion coleccion
collectionVivienda = db['viviendas']

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
#*PAGE ERROR
@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'


# ******************************************
#*MAIN
if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)