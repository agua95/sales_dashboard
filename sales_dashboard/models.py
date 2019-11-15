from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class Region(models.Model):
    region_name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.region_name

    @property
    def sales(self):
        return Sale.objects.filter(prop_name__region_name=self).count()

class Property(models.Model):
    prop_name = models.CharField(max_length=200)
    region_name = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Region")
    prop_code = models.IntegerField(default=0, verbose_name="Property")
    
    def __str__(self):
        return self.prop_name

    @property
    def sales(self):
        return Sale.objects.filter(prop_name=self).count()
    

class Sale(models.Model):
    prop_name = models.ForeignKey(Property, on_delete=models.CASCADE)
    employee = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Person")
    prop_state = models.CharField(null=True, max_length=5, choices=[('new','New'),('used','Used')])
    date = models.DateField('Sale Date')
    def __str__(self):
        return 'Congrats %s for a %s sale at %s!' % (self.employee, self.prop_state, self.prop_name.prop_code )

class Person(User):
    class Meta:
        proxy = True
    
    def sales(self):
        return Sale.objects.filter(employee=self).count()
    def name(self):
        return self

class Posts(models.Model):
    employee = models.ForeignKey(User, on_delete= models.CASCADE)
    prop_state = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prop_code = models.ForeignKey(Property, on_delete=models.CASCADE)
    def __str__(self):
        return f"Congrats {self.employee.username} for a {self.prop_state.prop_state} at {self.prop_code.prop_code}"