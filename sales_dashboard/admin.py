from django.contrib import admin
from import_export import resources
# Register your models here.
from .models import Region, Property, Sale, Goal
from import_export.admin import ImportExportModelAdmin
class RegionResource(resources.ModelResource):
    class Meta:
        model = Region
        fields = ('region_name',)

class PropertyResource(resources.ModelResource):
    class Meta:
        model = Property
        fields = ('prop_name', 'region_name', 'prop_code')

class SaleResource(resources.ModelResource):
    class Meta:
        model = Sale
        fields = ('prop_name', 'employee_name', 'prop_state', 'date')

class RegionAdmin(ImportExportModelAdmin):
    resource_class= RegionResource

class PropertyAdmin(ImportExportModelAdmin):
    resource_class= PropertyResource

class SaleAdmin(ImportExportModelAdmin):
    resource_class= SaleResource

admin.site.register(Region, RegionAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Goal)