from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields import BigIntegerField, DateField
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.contrib.auth.models import User

# Create your models here.


class Department(models.Model):
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name

class Designation(models.Model):
    designation_name = models.CharField(max_length=100)

    def __str__(self):
        return self.designation_name


class EmplopyeeDetails(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=100)
    email = models.EmailField()
    current_address = models.CharField(max_length=200)
    permanent_address = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    mobile_number = models.BigIntegerField(null=True)
    date_of_birth = models.DateField(null=True, auto_created=True)
    qualification = models.FileField(upload_to="qualifications", null=True,)
    department_name = models.ForeignKey(
        Department, null=True, on_delete=models.SET_NULL, 
        related_name="dept")
    designation = models.ForeignKey(
        Designation, null=True, on_delete=models.SET_NULL, 
        related_name="designation")
    aadhar_number = models.BigIntegerField(null=True)
    aadhar_copy = models.FileField(upload_to="aadhars", null=True)
    bank_name = models.CharField(max_length=200, null=True)
    bank_acc_number = models.BigIntegerField(null=True)
    pan_number = models.BigIntegerField(null=True)
    pan_copy = models.FileField(upload_to="pans", null=True)
    tax_saving_declarations_and_proofs = models.FileField(upload_to="tax_uploads", null=True)
    basic_salary = models.BigIntegerField(null=True)
    date_created = models.DateField(auto_created=True)
    date_join = models.DateField(null=True)

    def __str__(self):
        return str(self.pk)


class Payroll(models.Model):
    employee_id = models.ForeignKey(EmplopyeeDetails, on_delete=CASCADE,
                                related_name="emp_pk")
    payroll_month = models.CharField(max_length=15)
    payroll_year = models.BigIntegerField(null=True)
    work_days = models.IntegerField(null=True)
    P_T = models.FloatField(null=True)
    net_salary = models.FloatField(null=True, default=0)
    basic_salary = models.FloatField(null=True)
    bonus = models.FloatField(null=True)
    HRA = models.FloatField(null=True)
    CONVEYANCE = models.FloatField(null=True)
    LTA = models.FloatField(null=True)
    FBP = models.FloatField(null=True)
    Incentives = models.FloatField(null=True)
    TDS = models.FloatField(null=True)
    salary_Adv = models.FloatField(null=True)
    PF = models.FloatField(null=True)
    advance = models.FloatField(null=True)
    gross_salary = models.FloatField(null=True, default=0)
    total_deductions = models.FloatField(null=True, default=0)
    date_cretaed = models.DateField(auto_now=True)
    pdfs = models.FileField(upload_to="payslip_pdfs", null=True)

    def __str__(self):
        return str(self.employee_id)

    def save(self, *args, **kwargs):
        # calculate sum before saving
        self.gross_salary = self.calculate_gross()
        self.total_deductions = self.calculate_deduc()
        self.net_salary = self.gross_salary - self.total_deductions
        super(Payroll, self).save(*args, **kwargs)

    def calculate_gross(self):
        try:
            value_a = self.basic_salary
            value_b = self.bonus
            value_d = self.HRA
            value_e = self.LTA
            value_f = self.CONVEYANCE
            value_g = self.FBP
            value_h = self.Incentives
            gross = value_a + value_b + value_d + value_e + value_f + value_g + value_h
            return gross
        except KeyError:
            # Value_a or value_b is not in the VALUES dictionary.
            # Do something to handle this exception.
            # Just returning the value 0 will avoid crashes, but could 
            # also hide some underlying problem with your data.
            return 0

    def calculate_deduc(self):
        try:
            value_c = self.P_T
            value_i = self.TDS
            value_j = self.salary_Adv
            value_k = self.PF
            value_l = self.advance
            deduc = value_c + value_i + value_j + value_k + value_l
            return deduc
        except KeyError:
            # Value_a or value_b is not in the VALUES dictionary.
            # Do something to handle this exception.
            # Just returning the value 0 will avoid crashes, but could 
            # also hide some underlying problem with your data.
            return 0
    

class EmployeeAttendance(models.Model):
    E_Code = models.CharField(max_length=5)
    Name = models.CharField(max_length=100)
    Shift = models.CharField(max_length=2)
    InTime = models.TimeField(null=True)
    OutTime = models.TimeField(null=True)
    Work_Dur = models.TimeField(null=True)
    OT = models.TimeField(null=True)
    Tot_Dur = models.TimeField(null=True)
    Status = models.CharField(max_length=10)
    Remarks = models.TextField(max_length=300)

    def __str__(self):
        return self.E_Code
        

class EmployeeLeaves(models.Model):
    emplayee_name = models.CharField(max_length=100)
    leave_day_type = models.CharField(max_length=10)
    leave_type = models.CharField(max_length=2)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)
    leave_reason = models.TextField(max_length=500)
   


class Resignation(models.Model):
    employee_name = models.CharField(max_length=100)
    resign_reason = models.TextField(max_length=500)
    

class Messages(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    response = models.TextField(null=True)
    date = models.DateField(auto_now=True)
