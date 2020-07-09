from django.db import models
from django.utils import timezone
import os

class ModelNetworking(models.Model):
    # time_create = models.DateTimeField(default=timezone.now, blank=True)
    name_company = models.CharField(max_length=200, default='')
    representantes = models.CharField(max_length=200, default='')
    presence_online = models.CharField(max_length=200, default='')
    fecha_company = models.CharField(max_length=200, default='')
    tamano_company = models.CharField(max_length=200, default='')
    uri_reporte_tech = models.CharField(max_length=200, default='')
    uri_reporte_linkedin = models.CharField(max_length=200, default='')
    category = models.CharField(max_length=200, default='')
    tlf_contacto = models.CharField(max_length=200, default='')
    emails = models.CharField(max_length=200, default='')
    website_posible = models.CharField(max_length=200, default='')
    top_sites = models.CharField(max_length=200, default='')
    fanpage_fb = models.CharField(max_length=200, default='')
    web_server = models.CharField(max_length=200, default='')
    web_framework = models.CharField(max_length=200, default='')
    js_framework = models.CharField(max_length=200, default='')
    cms = models.CharField(max_length=200, default='')
    number_employers = models.CharField(max_length=200, default='')
    ruc = models.CharField(max_length=200, default='', unique=True)
    rubro = models.CharField(max_length=200, default='')
    direccion = models.CharField(max_length=200, default='')
    programming_languaje = models.CharField(max_length=200, default='')
    company_status = models.CharField(max_length=200, default='')
    twiter_page = models.CharField(max_length=200, default='')
    all_tech = models.CharField(max_length=800, default='')
    def __str__(self):
        return '{0}:{1}'.format(self.name_company, self.ruc)
