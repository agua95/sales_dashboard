import django_tables2 as tables
from .models import Sale, Region, Property, Person
from django_tables2.utils import Accessor

class MonthRegionTable(tables.Table):
    class Meta:
        model = Region
        template_name = "django_tables2/bootstrap.html"
        fields = ("region_name", "Monthly_Sales", )

class MonthPropertyTable(tables.Table):
    sales = tables.Column(verbose_name='Monthly Sales', orderable=True, accessor=Accessor('prop_name.Monthly_Sales'))
    class Meta:
        model = Property
        template_name = "django_tables2/bootstrap.html"
        fields = ("prop_name","prop_name.prop_code", "sales", )

class MonthPersonTable(tables.Table):
    sales = tables.Column(verbose_name='Monthly Sales', orderable=True, accessor=Accessor('employee.Monthly_Sales'))
    name = tables.Column(verbose_name='Salesperson', orderable=True, accessor=Accessor('employee.username'))
    class Meta:
        model = Person
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "sales", )

class YearRegionTable(tables.Table):
    class Meta:
        model = Region
        template_name = "django_tables2/bootstrap.html"
        fields = ("region_name", "Yearly_Sales", )

class YearPropertyTable(tables.Table):
    sales = tables.Column(verbose_name='Yearly Sales', orderable=True, accessor=Accessor('prop_name.Yearly_Sales'))
    class Meta:
        model = Property
        template_name = "django_tables2/bootstrap.html"
        fields = ("prop_name","prop_name.prop_code", "sales", )

class YearPersonTable(tables.Table):
    sales = tables.Column(verbose_name='Yearly Sales', orderable=True, accessor=Accessor('employee.Yearly_Sales'))
    name = tables.Column(verbose_name='Salesperson', orderable=True, accessor=Accessor('employee.username'))
    class Meta:
        model = Person
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "sales", )

class SalesFeedTable(tables.Table):
    class Meta:
        model = Sale
        template_name = "django_tables2/bootstrap.html"
        fields = ("feed", )
        