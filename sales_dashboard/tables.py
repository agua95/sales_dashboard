import django_tables2 as tables
from .models import Sale, Region, Property, Person

class SaleTable(tables.Table):
    class Meta:
        model = Sale
        template_name = "django_tables2/bootstrap.html"
        fields = ("prop_name.region_name","Sales", "prop_name.prop_code", "Sales", "employee", "Sales")


class RegionTable(tables.Table):
    class Meta:
        model = Region
        template_name = "django_tables2/bootstrap.html"
        fields = ("region_name", "sales", )

class PropertyTable(tables.Table):
    class Meta:
        model = Property
        template_name = "django_tables2/bootstrap.html"
        fields = ("prop_code", "sales", )

class PersonTable(tables.Table):
    class Meta:
        model = Person
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "sales", )

class SalesFeedTable(tables.Table):
    class Meta:
        model = Sale
        template_name = "django_tables2/bootstrap.html"
        fields = ("__str__", )
        