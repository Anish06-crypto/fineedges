# Generated by Django 3.1.7 on 2021-04-06 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginanddashboard', '0002_auto_20210406_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emplopyeedetails',
            name='mobile_number',
            field=models.CharField(max_length=10),
        ),
    ]
