#!/usr/bin/env python3

"""
    shebang is used for linux environment to support executing the file

    1 obtain info from ur
    2 save(add/update) info
    3 graphic info
    4 save data into table info
"""

# from urllib.request import urlopen
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime


def fetch_info(url):

    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    fecha_cot = soup.find('th', attrs = {'class':'fechaCot'})
    fecha = fecha_cot.text.strip()  # strip() is used to remove starting and trailing

    tabla_cotizacion = soup.find_all('table')[3]
    fila_valores =  tabla_cotizacion.find_all('tr')[1]

    valor_compra = fila_valores.find_all('td')[1].text
    valor_venta = fila_valores.find_all('td')[2].text

    # saves information into a csv file
    with open('info.csv','a+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([datetime.now(), fecha, valor_compra, valor_venta])


def main(url):
    data = fetch_info(url)

if __name__ == '__main__':
    url = 'http://www.bna.com.ar/'
    main(url) #the 0th argv is the module filename
