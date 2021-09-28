from django import forms
from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Department, Designation, EmplopyeeDetails, EmployeeAttendance, EmployeeLeaves, Payroll, Resignation


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class SendEmailForm(forms.Form):
        email = forms.EmailField()


class EmployeeAddForm(forms.ModelForm):
    class Meta:
        model = EmplopyeeDetails
        fields = "__all__"
        exclude = ['user', 'department_name', 'designation', 'basic_salary']


class DepartmentAddForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"


class DesignationAddForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = "__all__"


class LeaveApplyForm(forms.ModelForm):
    class Meta:
        model = EmployeeLeaves
        fields = "__all__"


class ResignationApplyForm(forms.ModelForm):
    class Meta:
        model = Resignation
        fields = "__all__"


class PayrollCalForm(forms.ModelForm):
    class Meta:
        model = Payroll
        exclude = ["net_salary", "gross_salary", "total_deductions"]
        







