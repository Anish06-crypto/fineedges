from fineedges import settings
from django import views
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

from . import views
import loginanddashboard

urlpatterns = [
    path("login", views.loginPage, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path("register", views.registerPage, name="register"),

    path("home", views.home, name="home"),
    path("user", views.userPage, name="user_page"),

    path('upload-details', views.settings, name="account"),
    path('responses', views.responses, name="responses"),
    path('<str:pk>/response-delete', views.deleteResponse, name="response_delete"),

    path("employee-attendance", login_required(login_url='login')(views.emp_upload), name="empupload"),

    path("<int:pk>/employee-update", login_required(login_url='login')(views.EmployeeUpdateView.as_view()), name="empupdate"),
    path("<int:pk>/employee-delete", login_required(login_url='login')(views.EmployeeDeleteView.as_view()), name="empdelete"),
    path("<int:pk>/employee-more", login_required(login_url='login')(views.EmpViewMoreView.as_view()), name="empviewmore"),

    path("department-add",login_required(login_url='login')(views.DepartmentAddView.as_view()), name="depadd"),
    path("<int:pk>/dept-update", login_required(login_url='login')(views.DepartmentUpdateView.as_view()), name="depupdate"),
    path("<int:pk>/dept-delete", login_required(login_url='login')(views.DepartmentDeleteView.as_view()), name="depdelete"),

    path("designation-add", login_required(login_url='login')(views.DesignationAddView.as_view()), name="desadd"),
    path("<int:pk>/designation-update", login_required(login_url='login')(views.DesignationUpdateView.as_view()), name="desupdate"),
    path("<int:pk>/designation-delete", login_required(login_url='login')(views.DesignationDeleteView.as_view()), name="desdelete"),

    path("employee-leaves", login_required(login_url='login')(views.LeaveApplyView.as_view()), name="emplev"),
    path("leave-update", login_required(login_url='login')(views.EmployeeLeaveResponseView.as_view()), name="leavereason"),
    path("<int:pk>/leave-okay", login_required(login_url='login')(views.LeaveOkayView.as_view()), name="levokay"),

    path("employee-resignation", login_required(login_url='login')(views.ResignApplyView.as_view()), name="empres"),
    path("resign-update", login_required(login_url='login')(views.EmployeeResignResponseView.as_view()), name="resignreason"),
    path("<int:pk>/resign-okay", login_required(login_url='login')(views.ResignOkayView.as_view()), name="resokay"),

    path("employee-list", login_required(login_url='login')(views.EmployeeListView.as_view()), name="emplist"),
    path("department-list", login_required(login_url='login')(views.DepartmentListView.as_view()), name="deplist"),
    path("employee-leaves-list", login_required(login_url='login')(views.EmployeeLeavesView.as_view()), name="emplevlist"),
    path("employee-resign-list", login_required(login_url='login')(views.EmployeeResignView.as_view()), name="empreslist"),
    path("designation-list", login_required(login_url='login')(views.DesignationListView.as_view()), name="deslist"),

    path("payroll-cal", login_required(login_url='login')(views.PayrollCalView.as_view()), name="paycal"),
    path("payslip-list", login_required(login_url='login')(views.PaySlipListView.as_view()), name="payslip-list"),
    path("payslip/<int:pk>", login_required(login_url='login')(views.PaySlipDetailView.as_view()),name="payslip"),
    path("<int:pk>/pay-delete", login_required(login_url='login')(views.PayslipDeleteView.as_view()), name="paydelete"),

    # path("hierarchy", views.HIE, name="HIE"),
    # path("hierarchyuser", views.HIEUser, name="HIEUser"),

    path('<int:pk>/pdf_view/', views.render_to_pdf, name="pdf_view"),


    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="loginanddashboard/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="loginanddashboard/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="loginanddashboard/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="loginanddashboard/password_reset_done.html"), 
        name="password_reset_complete"),
] 
