import re
import requests as req
from bs4 import BeautifulSoup as bs
from detect_tech.run_detect import detect_tech

def scraper_website(web):
    numeros = []
    emails = []
    facebook_pages = ''
    twitter_pages = ''
    linkedin_pages = ''
    whatsapp_numbers = ''
    telegram = ''
    tech_website = ''

    try:
        headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
        numeros, emails, facebook_pages, twitter_pages  = [], [], [], []
        whatsapp_numbers, telegram = [], []
        page = req.get(web, timeout=30, headers=headers).content
        html = bs(page, 'html.parser')

        email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}'
        tags_href = html.find_all('a')
        for value in tags_href:
            if 'tel:' in str(value):
                if value['href']:
                    tel = value['href'].replace('tel:', '')
                    numeros.append(tel)
        emails = re.findall(email_pattern, str(html))
        number_tlf = re.findall(r"\+\d{0,3}\s?0?\d{7,10}" , str(html))
        number_tlf2 = re.findall(r"\+?\d{0,3}?\s?0?\d{3}\s\d{3}\s\d{3}", str(html))
        number_tlf3 =  re.findall(r"\+?\(?\d{0,3}\)?\s?0?\d{3}\s\d{4}", str(html))
        facebook_pages = re.findall(r"facebook.com[-\.A-Za-z0-9/]+", str(html))
        fb_pages = re.findall(r"fb.me[-\.A-Za-z0-9/]+", str(html))
        twitter_pages = re.findall(r"twitter.com[-\._A-Za-z0-9/]+", str(html))
        linkedin_pages = re.findall(r"linkedin.com[-\._A-Za-z0-9/]+", str(html))
        api_whatsapp = re.findall(r"api.whatsapp.com/send\?phone=([\d]+)", str(html))
        web_whatsapp = re.findall(r"web.whatsapp.com/send\?phone=([\d]+)", str(html))
        wame_whatsapp = re.findall(r"wa.me/([\d]+)", str(html))
        uri_telegram = re.findall(r"t.me/[-\._A-Za-z0-9/]+", str(html))

        if number_tlf:
            numeros.extend(number_tlf)
        if number_tlf2:
            numeros.extend(number_tlf2)
        if number_tlf3:
            numeros.extend(number_tlf3)
        if fb_pages:
            facebook_pages.extend(fb_pages)
        if api_whatsapp:
            whatsapp_numbers.extend(api_whatsapp)
        if wame_whatsapp:
            whatsapp_numbers.extend(wame_whatsapp)
        if web_whatsapp:
            whatsapp_numbers.extend(web_whatsapp)
        if uri_telegram:
            telegram.extend(uri_telegram)

        numeros = [n.replace(' ', '').strip() for n in numeros]
        numeros = list(set(numeros))
        emails = list(set(emails))
        facebook_pages = list(set(facebook_pages))
        twitter_pages = list(set(twitter_pages))
        linkedin_pages = list(set(linkedin_pages))
        whatsapp_numbers = list(set(whatsapp_numbers))
        telegram = list(set(telegram))

        if numeros:
            numeros = numeros[:3]
        if emails:
            emails = emails[:3]
        if facebook_pages:
            facebook_pages = 'https://' + facebook_pages[0]
        if twitter_pages:
            twitter_pages = 'https://' + twitter_pages[0]
        if linkedin_pages:
            linkedin_pages = 'https://' + linkedin_pages[0]
        if whatsapp_numbers:
            whatsapp_numbers = '+' + whatsapp_numbers[0]
        if telegram:
            telegram = 'https://' + telegram[0]
    except Exception as e:
        print(e)

    tech_website = detect_tech(web)

    print(web, tech_website, numeros, emails, facebook_pages, twitter_pages, linkedin_pages, whatsapp_numbers, telegram)
    return(web, tech_website, numeros, emails, facebook_pages, twitter_pages, linkedin_pages, whatsapp_numbers, telegram)
