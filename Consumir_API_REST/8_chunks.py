import requests
import json

if __name__== '__main__':
    url = 'http://i.imgur.com/n9z3sLg.jpg'

    response = requests.get(url, stream=True)#Realiza la peticion sin descargar el contenido
    with open('imagen.jpg', 'wb') as file:
        for chunk in response.iter_content():#Descarga el contenido poco a poco
            file.write(chunk)
    
    response.close()#No olvidar cerrar la conexion