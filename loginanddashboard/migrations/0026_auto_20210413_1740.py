# Generated by Django 3.1.7 on 2021-04-13 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginanddashboard', '0025_auto_20210413_1714'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Allowances',
        ),
        migrations.DeleteModel(
            name='Deductions',
        ),
    ]
