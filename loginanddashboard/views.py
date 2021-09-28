from pathlib import Path
from loginanddashboard.resources import EmployeeResource
from typing import List
from loginanddashboard.forms import CreateUserForm, DepartmentAddForm, DesignationAddForm, DesignationAddForm, EmployeeAddForm, LeaveApplyForm, PayrollCalForm, ResignationApplyForm, SendEmailForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from django.forms.formsets import formset_factory
from tablib import Dataset
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives, message
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from fineedges.settings import EMAIL_HOST_USER
from django.conf import settings

from email.mime.image import MIMEImage
from django.contrib.staticfiles import finders
from functools import lru_cache

from . import models
from . import forms
from . import tables
from . import decorators

# Create your views here.

@decorators.unauthenticated_user
def registerPage(request):
            form = CreateUserForm()
            if request.method == 'POST':
                form = CreateUserForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    username = form.cleaned_data.get('username')

                    messages.success(request, 'Account was created for ' + username)

                    return redirect('login')
                

            context = {'form':form}
            return render(request, "loginanddashboard/register.html", context)


@decorators.unauthenticated_user
def loginPage(request):
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request,  "loginanddashboard/login.html", context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
@decorators.admin_only
def home(request):
	employees = models.EmplopyeeDetails.objects.all()

	total_employees = employees.count()

	context = {'employees':employees,
	'total_employees':total_employees }

	return render(request,  "loginanddashboard/home.html", context)

@login_required(login_url='login')
@decorators.allowed_users(allowed_roles=['employees','HR','HOD'])
def userPage(request):
    
    context = {}
    return render(request, "loginanddashboard/user.html", context)


@login_required(login_url='login')
@decorators.allowed_users(allowed_roles=['employees','HOD','HR'])
def settings(request):
    employee = request.user.emplopyeedetails
    form = EmployeeAddForm(instance=employee)

    if request.method == 'POST':
            form = EmployeeAddForm(request.POST, request.FILES,instance=employee)
            if form.is_valid():
                form.save()

    context = {'form': form}
    return render(request, "loginanddashboard/employee_upload_details.html", context)

@login_required(login_url='login')
@decorators.allowed_users(allowed_roles=['employees','HOD','HR'])
def responses(request):
    try:
        employee = request.user.messages

        context = {'employee': employee }
        return render(request, "loginanddashboard/leave_reject.html", context)
    except AttributeError:
        return HttpResponse('You have no new messages')


@login_required(login_url='login')
@decorators.allowed_users(allowed_roles=['employees','HOD','HR'])
def deleteResponse(request, pk):
	order = models.Messages.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/user')

	context = {'item':order}
	return render(request, 'loginanddashboard/response_delete.html', context)
   
    

class EmployeeAddView(CreateView):
    template_name = "loginanddashboard/employee_add.html"
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','admin']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.EmplopyeeDetails
    form_class = EmployeeAddForm
    success_url = "/employee-list"
    

class DepartmentAddView(CreateView):
    template_name = "loginanddashboard/department_add.html"
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','admin']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.Department
    form_class = DepartmentAddForm
    success_url = "/department-list"


class DesignationAddView(CreateView):
    template_name = "loginanddashboard/designation_add.html"
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','admin']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.Designation
    form_class = DesignationAddForm
    success_url = "/designation-list"


class LeaveApplyView(CreateView):
    template_name = "loginanddashboard/employee_leaves.html"
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','HOD','employees']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.EmployeeLeaves
    form_class = LeaveApplyForm
    success_url = "/employee-leaves"


class ResignApplyView(CreateView):
    template_name = "loginanddashboard/employee_resignation.html"
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','HOD','employees']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.Resignation
    form_class = ResignationApplyForm
    success_url = "/employee-resignation"


class ThankYouView(TemplateView):
    template_name = "loginanddashboard/thank-you.html"


class EmployeeListView(ListView):
    template_name = "loginanddashboard/employee_list.html"
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','HOD','admin']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.EmplopyeeDetails
    context_object_name = "emplist"
    


class DepartmentListView(ListView):
    template_name = "loginanddashboard/department_list.html"
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','HOD','admin']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.Department
    context_object_name = "departments"


class DesignationListView(ListView):
    template_name = "loginanddashboard/designation_list.html"
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','HOD','admin']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.Designation
    context_object_name = "design"


class PayrollCalView(CreateView):
    template_name = "loginanddashboard/payroll_cal.html"
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','admin']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.Payroll
    form_class = PayrollCalForm
    success_url = "/payslip-list"


class PaySlipListView(ListView):
    template_name = "loginanddashboard/payslip_list.html"
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','admin']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.Payroll
    context_object_name = "employees_pay"


class PaySlipDetailView(DetailView):
    template_name = "loginanddashboard/payslip.html"
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','admin']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.Payroll


class EmployeeLeavesView(ListView):
    template_name = "loginanddashboard/employee_leaves_list.html"
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','admin']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.EmployeeLeaves
    context_object_name = "leaves"


class EmployeeResignView(ListView):
    template_name = "loginanddashboard/employee_resign_list.html"
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','admin']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.Resignation
    context_object_name = "resigns"


class EmployeeUpdateView(UpdateView):
    template_name = 'loginanddashboard/employee_update.html'
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','admin']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.EmplopyeeDetails
    fields = "__all__"
    success_url = "/employee-list"


class DepartmentUpdateView(UpdateView):
    template_name = 'loginanddashboard/dept_update.html'
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','admin']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.Department
    fields = "__all__"
    success_url = "/department-list"


class DesignationUpdateView(UpdateView):
    template_name = 'loginanddashboard/des_update.html'
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','admin']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.Designation
    fields = "__all__"
    success_url = "/designation-list"


class EmployeeLeaveResponseView(CreateView):
    template_name = 'loginanddashboard/employee_leave_update.html'
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','admin']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.Messages
    fields = ["user", "response"]
    success_url = "/employee-leaves-list"


class EmployeeDeleteView(DeleteView):
    template_name = "loginanddashboard/emp_delete.html"
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','admin']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.EmplopyeeDetails
    success_url = "/employee-list"


class PayslipDeleteView(DeleteView):
    template_name = "loginanddashboard/pay_delete.html"
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','admin']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.Payroll
    success_url = "/payslip-list"


class DesignationDeleteView(DeleteView):
    template_name = "loginanddashboard/des_delete.html"
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','admin']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.Designation
    success_url = "/designation-list"


class DepartmentDeleteView(DeleteView):
    template_name = "loginanddashboard/dept_delete.html"
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','admin']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.Department
    success_url = "/department-list"


class LeaveResponseView(DetailView):
    template_name = "loginanddashboard/leave_reject.html"
    @method_decorator(decorators.allowed_users(allowed_roles=['HOD','employees']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.EmployeeLeaves


class LeaveOkayView(DeleteView):
    template_name = "loginanddashboard/leave_okay.html"
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','admin']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.EmployeeLeaves
    success_url = "/leave-update"


class EmpViewMoreView(DetailView):
    template_name = "loginanddashboard/emp_view_more.html"
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','admin']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.EmplopyeeDetails
    context_object_name = "employee_obj"


class EmployeeResignResponseView(CreateView):
    template_name = 'loginanddashboard/employee_resign_update.html'
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','admin']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.Messages
    fields = ["user","response"]
    success_url = "/employee-resign-list"


class ResignResponseView(DetailView):
    template_name = "loginanddashboard/resign_reject.html"
    @method_decorator(decorators.allowed_users(allowed_roles=['HOD','employees']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.Resignation


class ResignOkayView(DeleteView):
    template_name = "loginanddashboard/resign_okay.html"
    @method_decorator(decorators.allowed_users(allowed_roles=['HR','admin']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.Resignation
    success_url = "/resign-update"


def emp_upload(request):
    if request.method == 'POST':
        employee_resource = EmployeeResource()
        dataset = Dataset()
        new_employee = request.FILES['myfile']

        if not new_employee.name.endswith('xlsx'):
            messages.info(request, 'wrong format')
            return render(request, 'loginanddashboard/employee_list.html')

        imported_data = dataset.load(new_employee.read(),format='xlsx')
        for data in imported_data:
            value = models.EmployeeAttendance(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10]
            )  
        value.save()
    return render(request, 'loginanddashboard/attendance.html')


# @login_required(login_url='login')
# @decorators.allowed_users(allowed_roles=['HR','admin'])
# def HIE(request):
    
#     context = {}
#     return render(request, "loginanddashboard/hierarchyadmin.html", context)


# @login_required(login_url='login')
# @decorators.allowed_users(allowed_roles=['employees','HOD'])
# def HIEUser(request):
    
#     context = {}
#     return render(request, "loginanddashboard/hierarchyuser.html", context)

    
from io import BytesIO #A stream implementation using an in-memory bytes buffer
                       # It inherits BufferIOBase
 
from django.http import HttpResponse
from django.template.loader import get_template
from io import StringIO 
 
#pisa is a html2pdf converter using the ReportLab Toolkit,
#the HTML5lib and pyPdf.
 
from xhtml2pdf import pisa  
from django.core.files.base import ContentFile
#difine render_to_pdf() function
 
def render_to_pdf(request, *args, **kwargs):
        pk = kwargs.get('pk')
        employee = get_object_or_404(models.Payroll, pk=pk)

        template_path = 'loginanddashboard/pdf.html'
        context = {'payroll' : employee}
        template = get_template(template_path)
        html = template.render(context)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        pdf = result.getvalue()
        filename = 'Payslip.pdf'
        
        mail_subject = 'Payslip'
        to_email = employee.employee_id.email
        email = EmailMultiAlternatives(
            mail_subject,
            "hello",
            EMAIL_HOST_USER,
            [to_email]
        )
        email.attach(filename, pdf, 'application/pdf')
        email.send(fail_silently=False)

        return render(request, 'loginanddashboard/thank-you.html')  