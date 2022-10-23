
#* RANDOM
import random
#* OS
import os
#* Libreria expresiones regulares
import re

import requests

from bs4 import BeautifulSoup

import lxml




class Soib():

    """
    CLASE SOIB, NOS PERMITIRÁ APLICAR LOS METODOS A LO QUE NECESITEMOS MEDIANTE EL OBJETO
    """

    def __init__(self, collection, soup):

        """
        CONTRUCTOR DE LA CLASE NOMBRECLASE
        """

        #* Collection mongoDB
        self.collection = collection

        #* Objeto BeautifulSoup
        self.soup = soup

    def informacion(self):

        info_sanitarios = {}

        titulo = self.soup.find('h1', class_='entry-title')

        if titulo:
            info_sanitarios['titulo'] = titulo.text
        else:
            info_sanitarios['titulo'] = None

            #* NOTAS IMPORTANTES SOBRE find_all= Podemos hacer una busqueda más directa en
            #*  find_all, donde mediante "re.compile()" podemos decirle que nos encuentre si
            #*  en esas etiquetas se encuentra la palabra que le indiquemos al "re.compile()",
            #*  ya sea con text=, que simplemente averiguará si se encuentra esa palabra dentro
            #*  de algún atributo o contenido. Pero si queremos saber si queremos encontrar esa
            #*  etiqueta especifica ya sea mediante attrs={} o class_=. usaremos re.compile() en el valor,
            #*  como en el siguiente ejemplo.
        fecha = self.soup.find('p', class_='post-meta').find_all('span', class_=re.compile('published'))

        if fecha:
            #* ME OBLIGO A HACER UN BUCLE PARA PODER IMPLEMENTARLE EL TEXT, GET_TEXT U GET. ESTO ES PORQUE ES UNA LISTA
            #* QUE FUE HECHA A PARTIR DE FIND_ALL
            for fe in fecha:

                info_sanitarios['fecha'] = fe.text
        else:
            info_sanitarios['fecha'] = None

        media = self.soup.find('div', class_='et_post_meta_wrapper')
        if media:
            imagenes = media.find_all('img')
            if len(imagenes) == 0:
                print('No hay imagenes')
            else:
                imagen = imagenes[-1]
                img_src = imagen.get('src')
                try:
                    img_req = requests.get(img_src)
                    if img_req.status_code == 200:
                        info_sanitarios['imagen'] = img_req.content
                    else:
                        info_sanitarios['imagen'] = None
                except:
                    print('No se puedo obtener la imagen')
        else:
            print('No se encontro media')

        return info_sanitarios


    def enlaces(self):

        enlacesLimpios = []

        enlaces = self.soup.find('div', class_='entry-content').find_all('a', attrs={'href':re.compile('http')})

        for i in enlaces:

            enlacesLimpios.append(i.get('href'))

        return enlacesLimpios
    
    
    
    
