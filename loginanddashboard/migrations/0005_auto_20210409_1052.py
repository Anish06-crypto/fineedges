# Generated by Django 3.1.7 on 2021-04-09 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginanddashboard', '0004_auto_20210409_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='emplopyeedetails',
            name='basic_salary',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='emplopyeedetails',
            name='role',
            field=models.IntegerField(null=True),
        ),
    ]
