# Generated by Django 3.1.7 on 2021-04-22 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginanddashboard', '0033_auto_20210421_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='resignation',
            name='response',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
