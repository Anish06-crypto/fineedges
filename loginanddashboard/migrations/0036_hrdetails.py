# Generated by Django 3.1.7 on 2021-04-22 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loginanddashboard', '0035_emplopyeedetails_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='HRDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(auto_created=True, null=True)),
                ('HR_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('current_address', models.CharField(max_length=200)),
                ('permanent_address', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=10)),
                ('mobile_number', models.BigIntegerField(null=True)),
                ('qualification', models.FileField(null=True, upload_to='qualifications')),
                ('aadhar_number', models.BigIntegerField(null=True)),
                ('aadhar_copy', models.FileField(null=True, upload_to='aadhars')),
                ('bank_name', models.CharField(max_length=200, null=True)),
                ('bank_acc_number', models.BigIntegerField(null=True)),
                ('pan_number', models.BigIntegerField(null=True)),
                ('pan_copy', models.FileField(null=True, upload_to='pans')),
                ('basic_salary', models.BigIntegerField(null=True)),
                ('date_created', models.DateField(auto_now=True)),
                ('department_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deptHR', to='loginanddashboard.department')),
                ('designation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='designationHR', to='loginanddashboard.designation')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
