from django.contrib import admin

# Register your models here.
from .models import contact , seller_info

admin.site.register(contact)
admin.site.register(seller_info)
