# Generated by Django 3.1.7 on 2021-04-15 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginanddashboard', '0031_auto_20210415_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='basic_salary',
            field=models.BigIntegerField(null=True),
        ),
    ]
