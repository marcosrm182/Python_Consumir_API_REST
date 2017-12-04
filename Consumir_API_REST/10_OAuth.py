#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

client_id = '2e6fd342a766d7f6j83d'
client_secret = '83262c2e966403f6hg4582e05fab9b4f16e64eb7'

#El code se saca de la siguiente url https://github.com/login/oauth/authorize?client_id=2e6fd342a766d7f6j83d&scope=repo
code = '9a7cww6h8kl554d88913'

if __name__== '__main__':

    url = 'https://github.com/login/oauth/access_token'
    payload = {'client_id': client_id, 'client_secret': client_secret, 'code': code}
    headers = {'Accept': 'application/json'}
    
    response = requests.post(url, json=payload, headers=headers)
    
    print('...')
    print('...')
    print('...')
    print('El token solo funciona una sola vez despues hay que volver a generar uno si se quiere volver a obtener')
    print('...')
    print('...')
    print('...')

    if response.status_code == 200:
        #print(response.json())
        response_json = response.json()

        access_token = response_json['access_token']
        print(access_token)