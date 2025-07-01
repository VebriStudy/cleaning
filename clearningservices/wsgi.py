import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cleanservices.settings')  # ← sesuai nama folder baru

application = get_wsgi_application()
