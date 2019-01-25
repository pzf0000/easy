from django.conf.urls import url
from django.contrib import admin
import os
import django
"""
To ensure that files containing nameko services can run independently.
"""
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
