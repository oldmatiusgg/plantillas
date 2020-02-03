FROM python:3-slim-buster

# Copiar el archivo del proyecto de requirements.txt con el nombr4e de las dependencias
COPY requirements.txt /

# Instalame lo de requirements.txt a python, es decir, las dependencia
RUN pip install -r /requirements.txt

# Ahora ya tendriamos instalado las librerias dentro del contenedor.
# Ahora haremos una copia dentro del contenedor, a una ruta con una carpeta
COPY src/ /app

# Ahora estableremos una ruta de trabajo, apra que todo lo que hagamos vaya a esa ruta
# en este caso, a la carpeta que recien copiamos en la linea anterior
WORKDIR /app

# define los puertos, es decir, un puerto preconfigurado para ese contenedor, que un futuro se pueda cambiar ya es otra cosa.
EXPOSE 5000

# Ahora como en la consola de CMD, daremos instrucciones que serían ejecutar, python3 y main.py
CMD [ "python3", "main.py" ]