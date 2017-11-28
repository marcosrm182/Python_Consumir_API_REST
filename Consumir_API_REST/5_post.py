import requests
import json

if __name__== '__main__':
    url = 'http://httpbin.org/post'
    payload = {
        'nombre': 'Marcos',
        'curso': 'Python',
        'nivel': 'intermedio'
        }

    response = requests.post(url, json=payload)
    #response = requests.post(url, data=json.dumps(payload))

    #json post se encarga de serializarlos
    #data tendremos que serializar nosotros
    print(response.url)

    if response.status_code == 200:
        print(response.content)