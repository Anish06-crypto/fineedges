# Generated by Django 3.1.7 on 2021-04-09 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginanddashboard', '0005_auto_20210409_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emplopyeedetails',
            name='aadhar_number',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='emplopyeedetails',
            name='pan_number',
            field=models.BigIntegerField(null=True),
        ),
    ]
