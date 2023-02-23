from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from django.apps import apps

for model in apps.get_app_config('core').get_models():
    try: admin.site.register(model)
    except AlreadyRegistered: pass