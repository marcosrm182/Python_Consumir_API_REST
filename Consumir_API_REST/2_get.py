import requests

if __name__== '__main__':
    url = 'https://www.google.com.mx/'
    response = requests.get(url)

    if response.status_code == 200:
        content = response.content
        print(content) #Imprimimos por pantalla el contenido de la respuesta

        #Creamos un fichero y lo llenamos con lo que hemos recuperado
        file = open('google.html', 'wb')
        file.write(content)
        file.close