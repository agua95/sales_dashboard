# Generated by Django 2.2.7 on 2019-11-21 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_dashboard', '0009_auto_20191121_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mnregion_goal', models.IntegerField(default=0, verbose_name='Monthly Region Sales Goal')),
                ('mnproperty_goal', models.IntegerField(default=0, verbose_name='Monthly Property Sales Goal')),
                ('mnperson_goal', models.IntegerField(default=0, verbose_name='Monthly Salesperson Sales Goal')),
                ('yrregion_goal', models.IntegerField(default=0, verbose_name='Annual Region Sales Goal')),
                ('yrproperty_goal', models.IntegerField(default=0, verbose_name='Annual Property Sales Goal')),
                ('yrperson_goal', models.IntegerField(default=0, verbose_name='Annual Salesperson Sales Goal')),
            ],
        ),
    ]