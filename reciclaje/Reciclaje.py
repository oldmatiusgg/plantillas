
#* RANDOM
import random
#* OS
import os
#*Date
# from datetime import date, time, datetime
import datetime


class Reciclaje():

    """
    CLASE NOMBRECLASE, NOS PERMITIRÁ APLICAR LOS METODOS A LO QUE NECESITEMOS MEDIANTE EL OBJETO
    """

    def __init__(self, collection, usuario, contrasenya, usuario_id):

        """
        CONTRUCTOR DE LA CLASE NOMBRECLASE
        """

        self.inicio = 0

        #* collection mongoDB
        self.collection = collection

        #* usuario de SESSION
        self.usuario = usuario

        #* contraseña de SESSION
        self.contrasenya = contrasenya

        #* id Usuario de MongoDB
        self.usuario_id = usuario_id


    # def perfil(self):


    #* Método Donaciones
    def crearEvento(self, lugar, fecha, capacidad, labor, descripcion, donacion):

        listaDatos = [lugar, fecha, capacidad, labor, descripcion, donacion]

        print(fecha.split('-'))

        anyo = fecha.split('-')[0]
        mes = fecha.split('-')[1]
        dia = fecha.split('-')[2].split('T')[0]
        hora = fecha.split('-')[2].split('T')[1]

        print(f'anyo: {anyo} y mes: {mes} y dia: {dia} y hora: {hora}')

        x = datetime.datetime.now()
        print(x)

        anyoActual = x.strftime("%Y")
        mesActual = x.strftime("%m")
        diaActual = x.strftime("%d")
        horaActual = x.strftime("%X")

        #* Mensaje que se enviará
        mensaje = ''

        #* Diccionario donde está la información para agregar el evento
        diccEvento = {
            'usuario_id': self.usuario_id,
            'lugar': lugar,
            'fecha': f'{anyo}-{mes}-{dia}',
            'horario': hora,
            'capacidad': capacidad,
            'labor': labor,
            'descripcion': descripcion,
            'donacion': donacion
        }


        # print(anyoActual)

        print(f'anyoActual: {anyoActual} y mesActual: {mesActual} y diaActual: {diaActual} y horaActual: {horaActual}')

        if int(anyo) < int(anyoActual):

            mensaje = 'Tienes que poner una fecha actual'

            return listaDatos, mensaje
        
        else:


            if donacion != '':

                mensaje = f'Esta la cantidad maxima de donación que has colocado: {donacion}'

                agregarEvento = self.collection.insert_one(diccEvento)

                return listaDatos, mensaje

            else:

                mensaje = 'Has decidido que la maxima cantidad de donación sea INFINITO'

                diccEvento['donacion'] = 'infinito'

                agregarEvento = self.collection.insert_one(diccEvento)

                return listaDatos, mensaje


    def evento(self, lugar, fecha, nombreEvento, labor, donacion):

        anyo = fecha.split('-')[0]
        mes = fecha.split('-')[1]
        dia = fecha.split('-')[2]

        diccEvento = {
            'lugar': lugar,
            'fecha': f'{anyo}-{mes}-{dia}',
            'labor': labor,
            'donacion': donacion
        }

        #* Lista donde agregamos las querys con la información
        listaQuery = []

        #* Querys de MONGODB, en donde se tiene todas las posibilidades si el usuario
        #* le da por buscar solo con la fecha, o lugar, o también labor o hasta los eventos que tienen una cantidad
        #* determinada de donación. Es decir, que le usuario tenga todas las posibilidades de busqueda, que no tenga que poner
        #* todos los campos del formulario de busqueda sino que busque por el filtro que el usuario quiera.
        buscarEvento = self.collection(diccEvento)

        for i in list(buscarEvento):

            listaQuery.append(i)

        if listaQuery != []:

            print(listaQuery[0])

            mensaje = 'Busqueda completa, es decir, todos los campos fueron completas en la búsqueda'

            return listaQuery[0], mensaje
        
        # else:

        #     listaQuery.clear()
