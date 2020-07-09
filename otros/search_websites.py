#!/usr/bin/env python3
import os, sys
from google import google
import textdistance
from extract_email_phone import info_contacto_website
from time import sleep
from random import choice
os.environ['DJANGO_SETTINGS_MODULE'] = 'networking.settings'
import django
django.setup()
from app.models import ModelNetworking


class SearchSite(object):
    def run(self, search_str, pag_init, pag_end, cms):
        pull = self.get_websites(pag_init, pag_end, search_str)
        data_contact = list(map(info_contacto_website, pull))
        for dt in data_contact:
            website, numeros, emails, facebook_pages, twitter_pages = dt
            self.save_in_db(website, numeros, emails, facebook_pages, twitter_pages, cms)

    def save_in_db(self, website_posible, tlf, emails, facebook_pages, twitter_pages, all_tech):
        try:
            ModelNetworking.objects.create(
                                            tlf_contacto = tlf,
                                            emails = emails,
                                            website_posible = website_posible,
                                            all_tech = all_tech,
                                            fanpage_fb= facebook_pages,
                                            twiter_page= twitter_pages
                                            )
            print('save in db.')
        except Exception as e:
            print(e)


    def get_websites(self, pag_init, pag_end, search_str):
        pull = []
        for pag in range(pag_init, pag_end+1):
            try:
                sleep(choice([45,55,65])) #produccion entre 45, 55, a 65, 70
                data = self.searc_google(pag, search_str)
                data = [self.get_domain(i) for i in data]
                data = self.list_black(data)
                for i in data:
                    if not (i in pull):
                        pull.append(i)
                        print(i)
            except Exception as e:
                print(e)
        return pull

    def searc_google(self, num_page, query):
        dt = google.search(query, num_page)
        dt = [i.link for i in dt]
        return dt

    def list_black(self, website):
        sites = [
                'facebook.com', 'youtube', 'linkedin', 'mercadolibre.com', 'datosperu.org',
                'prezi.com', 'deperu.com', 'twitter', 'universidadperu', 'wikipedia', 'gestion.pe',
                'paginasamarillas'
        ]
        in_list = [True for uri in sites if uri in website]
        if in_list:
            return ''
        else:
            return website

    def similary_text(self, query, candidat):
        query = query.lower()
        return textdistance.cosine.normalized_similarity(query, candidat)

    def get_domain(self, url):
        try:
            url = url.replace('https://', '').replace('http://', '').replace('www.', '')
            url = url.split('/')[0]
            return url
        except Exception as e:
            print(e)

SearchSite().run('site:*.myshopify.com peru', 1, 10, 'shopify')
