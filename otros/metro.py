"""
Crawler para metro.pe
"""
import re
import json
#import subprocess
import cfscrape
import requests as req
from bs4 import BeautifulSoup as bs
#from openpyxl import Workbook


URL = 'https://www.metro.pe/'


def __find_links(url=URL):
    try:
        response = req.get(url).content
        html = bs(response, 'html.parser')
        links = html.find_all('a', class_='item-link')
        print(links)
        with open('metro-categories.txt', 'a+') as f:
            for i in links:
                print(i.attrs)
                f.write(i.attrs['href'] + '\n')
            f.close()
    except AttributeError as ae:
        print(ae)
    except Exception as e:
        print(e)
