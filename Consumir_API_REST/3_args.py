import requests

if __name__== '__main__':
    url = 'http://httpbin.org/get'
    args = {
        'nombre': 'Marcos',
        'curso': 'Python',
        'nivel': 'intermedio'
        }

    response = requests.get(url, params=args)
    print(response.url)

    if response.status_code == 200:
        content = response.content
        print(content) #Imprimimos por pantalla el contenido de la respuesta
