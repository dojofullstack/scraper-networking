import os, sys, platform

hostname = platform.uname()[1].lower().strip()
if hostname == 'clasificador-ai':
	produccion = 1
else:
	produccion = 0

if produccion:
	sys.path.append("/home/henry/vex-scrapers-networking/")
	activate_this = "/home/henry/.virtualenvs/networking/bin/activate_this.py"
else:
	sys.path.append("/home/henry/git/vex-scrapers-networking//")
	activate_this = "/home/henry/.virtualenvs/networking/bin/activate_this.py"


os.environ["DJANGO_SETTINGS_MODULE"] = "networking.settings"

os.environ.setdefault("LANG", "en_US.UTF-8")
os.environ.setdefault("LC_ALL", "en_US.UTF-8")

exec(open(activate_this).read())

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
