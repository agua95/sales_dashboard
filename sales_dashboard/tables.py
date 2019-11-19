import django_tables2 as tables
from .models import Sale, Region, Property, Person

class MonthRegionTable(tables.Table):
    class Meta:
        model = Region
        template_name = "django_tables2/bootstrap.html"
        fields = ("region_name", "Monthly_Sales", )

class MonthPropertyTable(tables.Table):
    class Meta:
        model = Property
        template_name = "django_tables2/bootstrap.html"
        fields = ("prop_name.prop_code", "prop_name.Monthly_Sales", )

class MonthPersonTable(tables.Table):
    class Meta:
        model = Person
        template_name = "django_tables2/bootstrap.html"
        fields = ("employee.username", "employee.Monthly_Sales", )

class YearRegionTable(tables.Table):
    class Meta:
        model = Region
        template_name = "django_tables2/bootstrap.html"
        fields = ("region_name", "Yearly_Sales", )

class YearPropertyTable(tables.Table):
    class Meta:
        model = Property
        template_name = "django_tables2/bootstrap.html"
        fields = ("prop_name.prop_code", "prop_name.Yearly_Sales", )

class YearPersonTable(tables.Table):
    class Meta:
        model = Person
        template_name = "django_tables2/bootstrap.html"
        fields = ("employee.username", "employee.Yearly_Sales", )

class SalesFeedTable(tables.Table):
    class Meta:
        model = Sale
        template_name = "django_tables2/bootstrap.html"
        fields = ("feed", )
        