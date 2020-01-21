
#* RANDOM
import random
#* OS
import os


class nombreClase():

    """
    CLASE NOMBRECLASE, NOS PERMITIRÁ APLICAR LOS METODOS A LO QUE NECESITEMOS MEDIANTE EL OBJETO
    """

    def __init__(self, collection, usuario):

        """
        CONTRUCTOR DE LA CLASE NOMBRECLASE
        """

        self.inicio = 0

        #* Collection mongoDB
        self.collection = collection

        #* Usuario, solo si la vamos a usar un login en la aplicación
        self.usuario = usuario