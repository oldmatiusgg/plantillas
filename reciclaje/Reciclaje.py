
#* RANDOM
import random
#* OS
import os


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