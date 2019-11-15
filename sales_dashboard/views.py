from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Region, Property, Sale, Person
from django.views.generic import ListView
from django_tables2 import SingleTableView
from .tables import SalesFeedTable, RegionTable, PropertyTable, PersonTable
from django_tables2 import MultiTableMixin
from django.views.generic.base import TemplateView

def index(request):
    return HttpResponse("Hello, world. You're at the sales index.")


class SalesListView(MultiTableMixin, TemplateView):
    model = Sale, Region, Property, Person
    #table_class = SaleTable
    qs = Sale.objects.all()
    qs1 = Region.objects.all()
    qs2 = Property.objects.all()
    qs3 = Person.objects.all()
    tables = [
        RegionTable(qs1),
        PropertyTable(qs2),
        PersonTable(qs3),  
        SalesFeedTable(qs, )
    ]

    template_name = 'sales_dashboard/sales.html'

