from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(EmplopyeeDetails)
class ViewAdmin(ImportExportModelAdmin):
    pass

admin.register(EmployeeAttendance)
class ViewAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Payroll)
admin.site.register(EmployeeLeaves)
admin.site.register(Resignation)
admin.site.register(Messages)



