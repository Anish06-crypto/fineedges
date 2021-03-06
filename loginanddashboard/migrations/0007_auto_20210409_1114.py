# Generated by Django 3.1.7 on 2021-04-09 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginanddashboard', '0006_auto_20210409_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='emplopyeedetails',
            name='P_T',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='emplopyeedetails',
            name='qualification',
            field=models.FileField(null=True, upload_to='qualifications'),
        ),
        migrations.AlterField(
            model_name='emplopyeedetails',
            name='department_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dept', to='loginanddashboard.department'),
        ),
    ]
