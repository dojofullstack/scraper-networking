#!/usr/bin/env python3
from google import google
import textdistance
num_page = 1
website_related = []
website_company = []

class SearchSiteCompany(object):
    def run(self, name_company):
        # print(name_company)
        data = self.searc_google(1, name_company)
        data = [self.get_domain(i) for i in data]
        top_sites, website = self.analize(data, name_company)
        # print(top_sites,website)
        return(top_sites, website)

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
            return url
        except Exception as e:
            print(e)

    def top_uris(self, item):
        if item[0] >= 40:
            return True
        else:
            return False

    def website_probabilty(self, item):
        if item[0] >= 70:
            return item[1]
        else:
            return ''

    def analize(self, uris, query):
        """ return fuentes relacionadas y fuente oficial posible """
        try:
            ft_, wst = [], ''
            ft_ = [self.similary_text(query, i)*100 for i in uris]
            ft_ = list(zip(ft_, uris))
            ft_ = filter(self.top_uris, ft_)
            ft_ = sorted(ft_)
            ft_.reverse()
            wst = self.website_probabilty(ft_[0])
            ft_ = [i[1] for i in ft_]
            wst = self.list_black(wst)
            return ft_[:8], wst
        except Exception as e:
            return '', ''

# SearchSiteCompany().run('triathlon ')
