# Generated by Django 3.1.7 on 2021-05-09 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginanddashboard', '0049_auto_20210509_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='emplopyeedetails',
            name='date_join',
            field=models.DateField(null=True),
        ),
    ]
