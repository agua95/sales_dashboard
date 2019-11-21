from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Region, Property, Sale, Person
from django.views.generic import ListView
from .tables import SalesFeedTable, MonthRegionTable, MonthPropertyTable, MonthPersonTable, YearRegionTable, YearPropertyTable, YearPersonTable
from django_tables2 import MultiTableMixin, SingleTableView
from django.views.generic.base import TemplateView
from datetime import datetime

def index(request):
    return HttpResponse("Hello, world. You're at the sales index.")


class SalesListView(MultiTableMixin, TemplateView):
    model = Sale, Region, Property, Person
    template_name = 'sales_dashboard/sales.html'
    qs = Sale.objects.all()
    mq = Sale.objects.filter(date__month = datetime.today().month)

    test = Sale.objects.filter(date__month = datetime.today().month).values_list('employee__username', flat = True).distinct()
    qs1 = Region.objects.all()
    yq = Sale.objects.filter(date__year = datetime.today().year)
    qs2 = Property.objects.all()
    qs3 = Person.objects.all()
    tables = [
        MonthRegionTable(qs1),
        MonthPropertyTable(mq),
        MonthPersonTable(mq),
        YearRegionTable(qs1),
        YearPropertyTable(yq),
        YearPersonTable(yq),
        SalesFeedTable(qs)    
    ]
    
    def regions(self):
        return Region.objects.all().order_by('region_name')

