import requests
import json

if __name__== '__main__':
    #url = 'http://httpbin.org/put'
    url = 'http://httpbin.org/delete'
    payload = {
        'nombre': 'Marcos',
        'curso': 'Python',
        'nivel': 'intermedio'
        }

    headers = {
        'Conten-Type': 'application/json',
        'acces-token': '12345'
        }

    #response = requests.put(url, json=payload, headers=headers)
    response = requests.delete(url, json=payload, headers=headers)
    print(response.url)

    if response.status_code == 200:
        #print(response.content)

        headers_response = response.headers #Diccionario
        server = headers_response['Server']
        
        print(server)