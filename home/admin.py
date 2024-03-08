from django.contrib import admin

# Register your models here.
from .models import seller_info,Contact

admin.site.register(seller_info)
admin.site.register(Contact)
