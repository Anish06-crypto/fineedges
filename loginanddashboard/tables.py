from django.db.models import fields
import django_tables2 as tables
from .models import Department, Designation, EmplopyeeDetails, EmployeeLeaves, Resignation

class EmployeeTable(tables.Table):
    class Meta:
        model = EmplopyeeDetails
        template_name = "django_tables2/bootstrap.html"
        fields = ("employee_name","designation", "department_name")

class DepartmentTable(tables.Table):
    class Meta:
        model = Department
        template_name = "django_tables2/bootstrap.html"
        fields = ("department_name", )


class DesignationTable(tables.Table):
    class Meta:
        model = Designation
        template_name = "django_tables2/bootstrap.html"
        fields = ("designation_name", "super_id")


class EmployeeLeaveTable(tables.Table):
    class Meta:
        model = EmployeeLeaves
        template_name = "django_tables2/bootstrap.html"
        exclude = ["reject_reason"]


class EmployeeResignTable(tables.Table):
    class Meta:
        model = Resignation
        template_name = "django_tables2/bootstrap.html"
        fields = ["ID" ,"employee_idr","employee_name","resign_reason"]




