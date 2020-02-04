
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
    def crearEvento(self, nombreEvento, lugar, fecha, capacidad, labor, descripcion, donacion):

        listaDatos = [nombreEvento, lugar, fecha, capacidad, labor, descripcion, donacion]

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
            'nombreEvento': nombreEvento,
            'lugar': lugar,
            'fecha': f'{anyo}-{mes}-{dia}',
            'horario': hora,
            'capacidad': capacidad,
            'labor': labor,
            'descripcion': descripcion,
            'donacion': int(donacion)
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


    def evento(self, nombreEvento, lugar, fecha, labor, donacion):

        

        #???????????????????????

        algunoEstaVacio = []

        diccEvento = {
            'nombreEvento': nombreEvento,
            'lugar': lugar,
            'fecha': fecha,
            'nombreEvento': nombreEvento, 
            'labor': labor, 
            'donacion': donacion
        }

        #* diccionario que me ayudará a realizar las querys de los datos no vacios.
        datosNoVacios = {}

        #* diccionario que me ayudará a realizar las querys de los datosvacios.
        datosVacios = {}

        for llave, i in diccEvento.items():

            if i != '':

                print('Los i"s que no estan vacios')

                print(f'{llave}: {i}')

                datosNoVacios[llave] = i

                # for llaveNoVacio, valorNoVacio in datosNoVacios.items():
                if 'fecha' in datosNoVacios:

                    anyo = fecha.split('-')[0]
                    mes = fecha.split('-')[1]
                    dia = fecha.split('-')[2]

                    datosNoVacios['fecha']: f'{anyo}-{mes}-{dia}' 

                else:

                    print('No se encuentra la llave FECHA en el diccionario de los datosNoVacios')

                if 'donacion' in datosNoVacios:

                    datosNoVacios['donacion']: int(donacion)

                else:

                    print('No se encuentra la llave DONACIÓN en el diccionario de los datosNoVacios')

                print(datosNoVacios)

                # #??????????????????????????????????????????????????????????????????

                # #* Lista donde agregamos las querys con la información
                listaQuery = []

                #* query de mongoDB con la lista datosNoVacios.
                buscarEvento = self.collection.find(datosNoVacios)

                print('Antes de que se haga el filtro, es decir, no se aplico el condicional IF')

                # #??????????????????????????????????????????????????????????????????

                # #* RECORDAR: Cuando le aplicamos list() a la variable que contiene la query, solo debemos hacerlo una vez, porque si lo hacemos más veces
                # #* entonces no te funcionará
                for i in list(buscarEvento):

                    listaQuery.append(i)

                if listaQuery != []:

                    print('Despues de que se aplique el filtro, es decir, si aparece este mensaje es que estas dentro del IF')

                    print(listaQuery[0])

                    mensaje = 'Busqueda completa, es decir, algún campo fue introducto o todos los campos/inputs se les fue introducido valores'

                    print(mensaje)

                    return listaQuery, mensaje


                # if llave == 'lugar' and llave == 

            else:

                #* Agregamos los datos vacios que el usuario no ingreso en la busqueda a la lista.

                algunoEstaVacio = [i]

        #???????????????????????????????????????
    
        for noValor in algunoEstaVacio:

            print('Los i"s que están vacios')

            print(noValor)

        return [diccEvento], 'Haciendo pruebas, no se introdujo ningún campo'
            # return listaQuery
        
        # else:

        #     listaQuery.clear()

        # return diccEvento

        #????????????????????????????


        # anyo = fecha.split('-')[0]
        #         mes = fecha.split('-')[1]
        #         dia = fecha.split('-')[2]

        #         diccEvento = {
        #             'lugar': lugar,
        #             'fecha': f'{anyo}-{mes}-{dia}',
        #             'labor': labor,
        #             'donacion': int(donacion)
        #         }

        #         print(diccEvento)

        #         #* Lista donde agregamos las querys con la información
        #         listaQuery = []

        #         #* Querys de MONGODB, en donde se tiene todas las posibilidades si el usuario
        #         #* le da por buscar solo con la fecha, o lugar, o también labor o hasta los eventos que tienen una cantidad
        #         #* determinada de donación. Es decir, que le usuario tenga todas las posibilidades de busqueda, que no tenga que poner
        #         #* todos los campos del formulario de busqueda sino que busque por el filtro que el usuario quiera.
        #         buscarEvento = self.collection.find(diccEvento)

        #         print('Antes de que se haga el filtro')

        #         # print(list(buscarEvento))

        #         #* RECORDAR: Cuando le aplicamos list() a la variable que contiene la query, solo debemos hacerlo una vez, porque si lo hacemos más veces
        #         #* entonces no te funcionará
        #         for i in list(buscarEvento):

        #             listaQuery.append(i)

        #         if listaQuery != []:

        #             print('Despues de que se aplique el filtro')

        #             print(listaQuery[0])

        #         mensaje = 'Busqueda completa, es decir, todos los campos/inputs se les fue introducido valores'

        #         print(mensaje)

        #         return listaQuery, mensaje

        
