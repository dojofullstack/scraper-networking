"""
Crawler para falabella
"""
import re
import json
import time
# import subprocess
import cfscrape
import requests as req
from bs4 import BeautifulSoup as bs
from app import database as db
# from openpyxl import Workbook
from lib.utils import driver

chrome = driver.chrome

products = db.conn.vexai.products

URL = 'https://www.falabella.com.pe/falabella-pe/'


def __find_links(url=URL):
    try:
        response = req.get(url).content
        html = bs(response, 'html.parser')
        links = html.find_all(
            'a', class_='fb-masthead__grandchild-links__item__link')
        print(links)
        with open('fala-categories.txt', 'a+') as f:
            for i in links:
                print(i.attrs)
                f.write(i.attrs['href'] + '\n')
            f.close()
    except AttributeError as ae:
        print(ae)
    except Exception as e:
        print(e)


def get_details(result, category_name):
    product = {
        'price': '',
        'title': '',
        'url': '',
        'category': '',
    }

    try:
        res_source = result.get_attribute('innerHTML')
        elements = bs(res_source, 'html.parser')
        price = elements.find_all('p', class_='fb-price')[-1].text.strip()
        title = elements.find(
            'h4', class_='fb-pod__product-title').text.strip()
        url = elements.find('h4', class_='fb-pod__product-title').a['href']

        product['price'] = price
        product['title'] = title
        product['category'] = str(category_name)
        product['url'] = f'https://www.falabella.com.pe{url}'
        # print(product)
        return product
    except Exception as e:
        print(e)


def get_last_page(cat_slug):
    ind_class_name = 'extreme-number'

    url = f'https://www.falabella.com.pe{cat_slug}'
    chrome.get(url)

   # body = req.get(url).content
   # html = bs(body, 'html.parser')
    # 'acc-alert-deny'
    btn = chrome.find_element_by_css_selector(
        'a#acc-alert-deny')

    btn.click()

    time.sleep(2)

    el = chrome.find_element_by_css_selector(
        'div.fb-filters-sort div.no-selected-number.extreme-number')

    page_number = bs(el.get_attribute('innerHTML'), 'html.parser')

    # last_page = html.find('div', class_=ind_class_name)

    print(el)
    return page_number


def scrap_category(cat_slug):
    list_to_save = []  # Para pasarle una lista a mongo
    try:
        url = f'https://www.falabella.com.pe{cat_slug}'

        body = req.get(url).content
        html = bs(body, 'html.parser')
        chrome.get(url)

        category_name = bs(chrome.find_element_by_class_name(
            'fb-filter-category').get_attribute('innerHTML'), 'html.parser')

        results = chrome.find_elements_by_class_name(
            'fb-pod__item')
        for res in results:
            parsed = get_details(res, category_name)
            list_to_save.append(parsed)

        print(list_to_save)
        products.insert_many(list_to_save)

    except Exception as e:
        print(e)


#total = []
#
# with open('fala-categories.txt', 'r') as slugs:
#    for s in slugs:
#        # print(s)
#        print(f'Scraping {s}')
#        total.append(scrap_category(s))
#    chrome.close()
#    slugs.close()
#
# print(len(total))

# print(products.insert_one({'hello': 'world'}))
# scrap_category('/falabella-pe/category/cat11000480/TV-LED')
# print(get_last_page('/falabella-pe/category/cat11000480/TV-LED'))
scrap_category('/falabella-pe/category/cat11000480/TV-LED')
