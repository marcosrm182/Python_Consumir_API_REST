#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#READ
#
#Solo lista mis repositorios de GitHub

import requests

client_id = '2e6fd342a766d7f6j83d'
client_secret = '83262c2e966403f6hg4582e05fab9b4f16e64eb7'

#El code se saca de la siguiente url https://github.com/login/oauth/authorize?client_id=2e6fd342a766d7f6j83d&scope=repo
code = '9a7cww6h8kl554d88913'
access_token = 'eb0ab89arg75hy812503bd23f52be9892a35d341'

if __name__== '__main__':
    url = 'http://api.github.com/user/repos'
    headers = { 'Authorization': 'token a7b7767y5g4r6721bd6b23451bd216d590c645b9' }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print('Ok')
        payload = response.json()

        for project in payload:
            name = project['name']
            print(name)
    else:
        print('Bad')
        print(response.status_code)