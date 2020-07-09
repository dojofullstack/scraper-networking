"""
Crawler para plazavea.com.pe
"""
import re
import json
#import subprocess
import cfscrape
import requests as req
from bs4 import BeautifulSoup as bs
#from openpyxl import Workbook

URL = 'https://www.plazavea.com.pe/'


def __find_links(url=URL):
    try:
        response = req.get(url).content
        html = bs(response, 'html.parser')
        links = html.find_all('a', class_='hmi-link')
        print(links)
        with open('plazavea-categories.txt', 'a+') as f:
            for i in links:
                print(i.attrs)
                f.write(i.attrs['href'] + '\n')
            f.close()
    except AttributeError as ae:
        print(ae)
    except Exception as e:
        print(e)


def scrap_categories(categories):
    try:
        response = req.get(url).content
        html = bs(response, 'html.parser')
        links = html.find_all('a', class_='hmi-link')
        print(links)
    except Exception as e:
        print(e)
