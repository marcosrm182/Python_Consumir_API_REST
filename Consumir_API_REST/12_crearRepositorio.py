#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

if __name__== '__main__':
    client_id = '2e6fd342a766d7b18b4f'
    client_secret = '83262c2e96648dc355e582e05fab9b4f16e64eb7'
    code = '9a7c2d060cc554d88913' #El code se saca de la siguiente url https://github.com/login/oauth/authorize?client_id=2e6fd342a766d7b18b4f&scope=repo

    access_token = 'eb0ab89a4ba8eac12503bd23f52be9892a35d341'

    url = 'https://api.github.com/user/repos'
    payload = { 'name': 'repo_desde_python' }
    headers = { 'Accept': 'application/json', 'Authorization': 'token ' + access_token }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print(response.json())
    else:
        print(response.content)

    print(response.status_code)