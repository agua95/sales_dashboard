from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
import random

class Goal(models.Model):
    mnregion_goal = models.IntegerField(default=0, verbose_name="Monthly Region Sales Goal")
    mnproperty_goal = models.IntegerField(default=0, verbose_name="Monthly Property Sales Goal")
    mnperson_goal = models.IntegerField(default=0, verbose_name="Monthly Salesperson Sales Goal")
    yrregion_goal = models.IntegerField(default=0, verbose_name="Annual Region Sales Goal")
    yrproperty_goal = models.IntegerField(default=0, verbose_name="Annual Property Sales Goal")
    yrperson_goal = models.IntegerField(default=0, verbose_name="Annual Salesperson Sales Goal")
 
class Region(models.Model):
    region_name = models.CharField(max_length=10, verbose_name="Region")
    
    def __str__(self):
        return self.region_name

    @property
    def Monthly_Sales(self):
        return Sale.objects.filter(prop_name__region_name=self, date__month=datetime.today().month).count()
    
    def Yearly_Sales(self):
        return Sale.objects.filter(prop_name__region_name=self, date__year=datetime.today().year).count()


class Property(models.Model):
    prop_name = models.CharField(max_length=200, verbose_name="Property")
    region_name = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Region")
    prop_code = models.IntegerField(default=0, verbose_name="Property Code")
    
    def __str__(self):
        return self.prop_name

    @property
    def Monthly_Sales(self):
        return Sale.objects.filter( prop_name=self, date__month = datetime.today().month).count()

    def Yearly_Sales(self):
        return Sale.objects.filter( prop_name=self, date__year = datetime.today().year).count()

class Person(User):
    class Meta:
        proxy = True
    
    def Monthly_Sales(self):
        return Sale.objects.filter(employee=self, date__month = datetime.today().month).count()

    def Yearly_Sales(self):
        return Sale.objects.filter(employee=self, date__year = datetime.today().year).count()

    def name(self):
        return self


class Sale(models.Model):
    prop_name = models.ForeignKey(Property, on_delete=models.CASCADE)
    employee = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name="Person")
    prop_state = models.CharField(null=True, max_length=5, choices=[('new','New'),('used','Used')])
    date = models.DateField('Sale Date')
    def feed(self):
        congrats = ['Congrats %s for a %s sale at %s!', 
            'Lets give it up to %s for getting a %s sale at %s!', 
            'A big high five to %s for getting a %s sale at %s!', 
            'Stellar job to %s for getting a %s sale at %s!' ]
        return  random.choice(congrats) % (self.employee, self.prop_state, self.prop_name )


class Posts(models.Model):
    employee = models.ForeignKey(User, on_delete= models.CASCADE)
    prop_state = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prop_code = models.ForeignKey(Property, on_delete=models.CASCADE)
    def __str__(self):
        return f"Congrats {self.employee.username} for a {self.prop_state.prop_state} at {self.prop_code.prop_code}"