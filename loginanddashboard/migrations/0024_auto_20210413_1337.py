# Generated by Django 3.1.7 on 2021-04-13 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginanddashboard', '0023_auto_20210413_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payroll',
            name='net_salary',
            field=models.FloatField(default=0, null=True),
        ),
    ]
