# Generated by Django 2.2.7 on 2019-11-21 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_dashboard', '0008_auto_20191118_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='prop_code',
            field=models.IntegerField(default=0, verbose_name='Property Code'),
        ),
        migrations.AlterField(
            model_name='property',
            name='prop_name',
            field=models.CharField(max_length=200, verbose_name='Property'),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_name',
            field=models.CharField(max_length=10, verbose_name='Region'),
        ),
    ]
