# Generated by Django 3.1.7 on 2021-04-09 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginanddashboard', '0011_auto_20210409_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emplopyeedetails',
            name='date_of_birth',
            field=models.DateField(auto_created=True, null=True),
        ),
    ]
