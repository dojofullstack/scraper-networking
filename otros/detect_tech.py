#!/usr/bin/env python3
import re
import json
import subprocess
import requests as req
from bs4 import BeautifulSoup as bs
from subprocess import Popen, PIPE
import json
import uuid
from random import randint
from time import sleep


def detect_tech(url):
    all_tech = ''
    url = url.replace('https://', 'http://')
    if not('http' in url):
        url = 'http://{}'.format(url)
    id_ = str(uuid.uuid4()).split('-')[0]
    name = '{}.json'.format(id_)
    rpt, web_server, programming_languaje, web_framework, js_framework, cms, uri_reporte = [], [], [], [], [], [], []
    cmd = 'sudo docker run --rm wappalyzer/cli {}'.format(url)
    cmd2 = 'wad -t 20 -u {}'.format(url)
    # cmd3 = 'curl --upload-file ./{0} https://transfer.sh/{1}'.format(name,name)

    try:
        proc = Popen(cmd2, shell=True, stdout=PIPE)
        rpt = proc.stdout.read().decode('utf-8')
        if len(rpt) >= 70:
            all_tech += rpt
            rpt = json.loads(rpt)
            for i,v in rpt.items():
                for k in v:
                    if 'web-servers' in k['type']:
                        web_server.append(k['app'])
                    if 'programming-languages' in k['type']:
                        programming_languaje.append(k['app'])
                    if 'web-frameworks' in k['type']:
                        web_framework.append(k['app'])
                    if 'javascript-frameworks' in k['type']:
                        js_framework.append(k['app'])
                    if 'cms' in k['type']:
                        cms.append(k['app'])
    except Exception as e:
        print(e)

    try:
        proc = Popen(cmd, shell=True, stdout=PIPE)
        rpt = proc.stdout.read().decode('utf-8')
        if len(rpt) >= 70:
            all_tech += rpt
            rpt = json.loads(rpt)
            for i in rpt['applications']:
                ctg = str(i['categories'][0]).lower()
                if 'web servers' in ctg:
                    web_server.append(i['name'])
                if 'web frameworks' in ctg:
                    web_framework.append(i['name'])
                if 'javascript frameworks' in ctg:
                    js_framework.append(i['name'])
                if 'cms' in ctg:
                    cms.append(i['name'])
                if 'programming languages' in ctg:
                    programming_languaje.append(i['name'])
    except Exception as e:
        print(e)

    # save reporte
    # with open(name, 'w') as f:
    #     f.write(rpt)

    # upload reporte
    # try:
    #     proc = Popen(cmd3, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
    #     uri_reporte = str(proc.stdout.read())
    # except:
    #     pass

    # print(web_server, programming_languaje, web_framework, js_framework, cms)
    all_tech = str(all_tech).lower()
    return(web_server, programming_languaje, web_framework, js_framework, cms, all_tech)


# detect_tech('http://159.65.96.225/classifier')
