
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

    def __init__(self, collection, usuario, contraseña):

        """
        CONTRUCTOR DE LA CLASE NOMBRECLASE
        """

        self.inicio = 0

        #* collection mongoDB
        self.collection = collection

        #* usuario de SESSION
        self.usuario = usuario

        #* contraseña de SESSION


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


        # print(anyoActual)

        print(f'anyoActual: {anyoActual} y mesActual: {mesActual} y diaActual: {diaActual} y horaActual: {horaActual}')

        if int(anyo) < int(anyoActual):

            mensaje = 'Tienes que poner una fecha actual'

            return mensaje
        
        else:


            if donacion != 0:

                return listaDatos

            else:

                donacion = 'Has decidido que la maxima cantidad de donación sea INFINITO'

                return listaDatos







        