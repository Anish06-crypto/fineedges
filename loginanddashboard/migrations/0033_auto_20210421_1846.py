# Generated by Django 3.1.7 on 2021-04-21 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginanddashboard', '0032_payroll_basic_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emplopyeedetails',
            name='confirm_password',
        ),
        migrations.RemoveField(
            model_name='emplopyeedetails',
            name='password',
        ),
        migrations.RemoveField(
            model_name='emplopyeedetails',
            name='role',
        ),
    ]
