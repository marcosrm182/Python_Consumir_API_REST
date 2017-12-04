#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

if __name__== '__main__':
    url = 'https://api.github.com/user'

    session = requests.session()
    session.auth = ( 'email@gmail.com', 'passwordGitHub ')

    response = session.get(url)

    if response.ok:
        response = session.get('https://github.com/usuarioGitHub')
        if response.ok:    
            print(response.content)
            print('...')
            print('...')
            print(response.cookies)
            print('...')
            print('...')
            print('Valor de la cookie _gh_sess')
            print('...')
            print(response.cookies['_gh_sess'])
    else:
        print(response.content)