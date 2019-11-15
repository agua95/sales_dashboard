from django.contrib import admin

# Register your models here.
from .models import Region, Property, Sale

admin.site.register(Region)
admin.site.register(Property)
admin.site.register(Sale)