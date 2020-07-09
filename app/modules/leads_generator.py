from serpapi.google_search_results import GoogleSearchResults
from time import sleep
import csv
from slugify import slugify
import os
from scraper_website  import scraper_website


def get_leads(query, country, engine, result):
    if not country == 'all':
        query = f'{query} site:{country}'
    result_page = 25
    pages = int(result / result_page)
    name_slug = slugify(query)
    filename = "leads/leads-{}.data".format(name_slug)
    links = set()
    cont_err = 0

    for page in range(pages):
        print('page:', page)
        sleep(0.1)
        try:
            client = GoogleSearchResults({"q": query,
                "serp_api_key": "8bbe8d18d0e1a4f503a547cfcfa4318b49be7e63ad308916c7657f31cd98831c",
                "engine": engine,
                "start": page * result_page,
                "num": result_page
              })
            result = client.get_dict()
            organic_results = [i.get('link') for i in  result.get('organic_results')]
            organic_results = ['{}//{}'.format(s.split('/')[0], s.split('/')[2]) for s in organic_results]
            for link in organic_results:
                print(link)
                links.add(link)
            print('numero de resultados : ', len(links))
        except Exception as e:
            cont_err += 1
            print(e)
            if cont_err >= 3:
                break

    print('Query: ', query)
    print('Numero de resultados:',  len(links))


get_leads('agencias diseño grafico', 'all',  'google', 50)

# t = 'https://www.cloudbits.org.mx/'
# scraper_website(t)
