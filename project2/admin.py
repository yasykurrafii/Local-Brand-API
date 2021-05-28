from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin



from .models import *

# Register your models here.

TokenAdmin.raw_id_fields = ['user']
admin.site.register(Brand)
admin.site.register(Type)
admin.site.register(Image)
admin.site.register(Product)