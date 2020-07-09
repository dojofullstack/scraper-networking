import re
from EmailHarvester import EmailHarvester
import requests as req
from bs4 import BeautifulSoup as bs


def info_contacto_website(web):
    if not('http' in web):
        if 'www' in web:
            web = 'http://{}'.format(web)
        elif not ('www' in web):
            web = 'http://www.{}'.format(web)

    # +56 2 2551 59 88 no detectado
    try:
        numeros, emails,facebook_pages, twitter_pages  = [], [], [], []
        page = req.get(web).content
        html = bs(page, 'html.parser')
        email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}'
        emails = re.findall(email_pattern, str(html))
        number_tlf = re.findall(r"\+\d{0,3}\s?0?\d{7,10}" , str(html))
        number_tlf2 = re.findall(r"\+?\d{0,3}?\s?0?\d{3}\s\d{3}\s\d{3}" , str(html))
        number_tlf3 =  re.findall(r"\+?\(?\d{0,3}\)?\s?0?\d{3}\s\d{4}", str(html))
        facebook_pages = re.findall(r"facebook.com[-\.A-Za-z0-9/]+", str(html))
        twitter_pages = re.findall(r"twitter.com[-\._A-Za-z0-9/]+", str(html))
        if number_tlf:
            numeros.extend(number_tlf)
        if number_tlf2:
            numeros.extend(number_tlf2)
        if number_tlf3:
            numeros.extend(number_tlf3)
        numeros = [n.replace(' ', '').strip() for n in numeros]
        numeros = list(set(numeros))
        facebook_pages = list(set(facebook_pages))
        twitter_pages = list(set(twitter_pages))
    except Exception as e:
        debug(e)
    try:
        more_emails = EmailHarvester.runing(web.replace('www.', '').replace('http://', '').replace('https://', '').replace('/', ''))
        emails.extend(more_emails)
    except Exception as e:
        debug(e)
    emails = list(set(emails))
    if emails:
        emails = [im for im in emails if not('22' in im) and not('jpg' in im) and not('png' in im)]
    print(web, numeros, emails, facebook_pages, twitter_pages)
    return(web, numeros, emails, facebook_pages, twitter_pages)



# info_contacto_website('vexsoluciones.com')
