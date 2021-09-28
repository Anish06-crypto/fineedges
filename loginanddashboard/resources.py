from import_export import resources
from .models import EmplopyeeDetails, EmployeeAttendance
 
class EmployeeResource(resources.ModelResource):
    class Meta:
        model = EmployeeAttendance