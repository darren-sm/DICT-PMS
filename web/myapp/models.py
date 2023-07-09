from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.



#Database Models--

#model for CPMS

class CPMS(models.Model):
    program = models.CharField(max_length=255, primary_key=True)
    info = models.JSONField(default=[{
        "Activity": "",
        "Indicator": "",
        "Target": None,
        "Accomplishment": None,
        "Remarks": ""
    },
    ])

    def __str__(self) -> str:
        return f"{self.program}"

#model for Examinees
class Examinees(models.Model):
    COMPONENT_CHOICES = [
        ('Hands-on Exam', 'Hands-on Exam'),
        ('Diagnostic Exam', 'Diagnostic Exam'),
        ('User Assessment', 'User Assessment'),
    ]

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    STATUS_CHOICES = [
        ('Passed', 'Passed'),
        ('Failed', 'Failed'),
        ('For checking', 'For checking'),
        ('For transmittal', 'For transmittal'),
    ]

    no = models.AutoField(primary_key=True)
    province = models.CharField(max_length=255)
    component = models.CharField(max_length=15, choices=COMPONENT_CHOICES)
    name = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date = models.DateField()
    time = models.CharField(max_length=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    remarks = models.CharField(max_length=255)
    batch = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"[{self.batch}] {self.name} - {self.province}"
    
#model for OJT
class OJTInput(models.Model):
    PROVINCE_CHOICES = [
        ('Cavite', 'Cavite'),
        ('Laguna', 'Laguna'),
        ('Batangas', 'Batangas'),
        ('Rizal', 'Rizal'),
        ('Quezon', 'Quezon'),
        ('RO', 'RO'),
    ]

    CATEGORY_CHOICES = [
        ('accepted at DICT Office', 'accepted at DICT Office'),
        ('endorsed by partners', 'endorsed by partners'),
    ]

    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    MODE_CHOICES = [
        ('Physical Reporting', 'Physical Reporting'),
        ('Online', 'Online'),
        ('Hybrid', 'Hybrid'),
    ]

    id = models.AutoField(primary_key=True)
    province = models.CharField(max_length=30, choices=PROVINCE_CHOICES)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    suc = models.CharField(max_length=255)
    duration = models.IntegerField()
    school_address = models.CharField(max_length=400)
    representative = models.CharField(max_length=255)
    representative_contact = models.CharField(max_length=15)
    student_name = models.CharField(max_length=255)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    student_contact = models.CharField(max_length=15)
    start_date = models.DateField()
    end_date = models.DateField()
    mode = models.CharField(max_length=20, choices=MODE_CHOICES)
    resume = models.BooleanField()
    endorsement = models.BooleanField()
    moa = models.BooleanField()
    remarks = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return f"{self.student_name} ({self.suc})"