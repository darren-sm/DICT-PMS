from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.



#Database Models--

#model for CPMS

class CPMS(models.Model):
    id = models.AutoField(primary_key=True),
    program = models.CharField(max_length=255)
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
    TIME_CHOICES = [
        ('AM','am'),
        ('PM','pm'),
    ]
    no = models.AutoField(primary_key=True)
    province = models.CharField(max_length=255)
    component = models.CharField(max_length=15, choices=COMPONENT_CHOICES)
    name = models.CharField(max_length=255)
    venue = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date = models.DateField(null=True)
    time = models.CharField(max_length=2, choices=TIME_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    remarks = models.CharField(max_length=255, blank=True)
    batch = models.CharField(max_length=255, blank=True)

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
        ('interns accepted', 'interns accepted'),
        ('interns completed', 'interns completed'),
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
    suc = models.CharField(max_length=255, blank=True)
    duration = models.IntegerField(blank=True)
    school_address = models.CharField(max_length=400, blank=True)
    representative = models.CharField(max_length=255, blank=True)
    representative_contact = models.CharField(max_length=15, blank=True)
    student_name = models.CharField(max_length=255)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    student_contact = models.CharField(max_length=15, blank=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    mode = models.CharField(max_length=20, choices=MODE_CHOICES)
    resume = models.BooleanField()
    endorsement = models.BooleanField()
    moa = models.BooleanField()
    remarks = models.CharField(max_length=255, blank=True)
    
    def __str__(self) -> str:
        return f"{self.student_name} ({self.suc})"
    
#model for TMD
class tmd(models.Model):
    PROVINCE_CHOICES = [
        ('Cavite', 'Cavite'),
        ('Laguna', 'Laguna'),
        ('Batangas', 'Batangas'),
        ('Rizal', 'Rizal'),
        ('Quezon', 'Quezon'),
        ('RO', 'RO'),
    ]

    CATEGORY_CHOICES = [
        ('ToT', 'ToT'),
        ('Digital Governance and Management', 'Digital Governance and Management'),
        ('Digital Transformative Technologies', 'Digital Transformative Technologies'),
        ('Cyber Security', 'Cyber Security'),
        ('Information Session', 'Information Session'),
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
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.CharField(max_length=20, blank = True)
    end_time = models.CharField(max_length=20, blank = True)
    duration = models.IntegerField()
    resource_person = models.CharField(max_length=255, blank=True)
    facilitator = models.CharField(max_length=255, blank=True)
    female = models.IntegerField(default=0)
    male = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    male_cavite = models.IntegerField(default=0)
    female_cavite = models.IntegerField(default=0)
    male_laguna = models.IntegerField(default=0)
    female_laguna = models.IntegerField(default=0)
    male_batangas = models.IntegerField(default=0)
    female_batangas = models.IntegerField(default=0)
    male_rizal = models.IntegerField(default=0)
    female_rizal = models.IntegerField(default=0)
    male_quezon = models.IntegerField(default=0)
    female_quezon = models.IntegerField(default=0)
    male_other = models.IntegerField(default=0)
    female_other = models.IntegerField(default=0)
    
    
    def __str__(self) -> str:
        return f"[{self.category}] {self.title}"
    
#model for EPMD
class epmd(models.Model):
    PROVINCE_CHOICES = [
        ('Cavite', 'Cavite'),
        ('Laguna', 'Laguna'),
        ('Batangas', 'Batangas'),
        ('Rizal', 'Rizal'),
        ('Quezon', 'Quezon'),
        ('RO', 'RO'),
    ]

    CATEGORY_CHOICES = [
        ('NGA', 'NGA'),
        ('LGU', 'LGU'),
        ('Industry', 'Industry'),
        ('SUC', 'SUC'),
        ('Training Institution', 'Training Institution'),
    ]
    


    id = models.AutoField(primary_key=True)
    province = models.CharField(max_length=30, choices=PROVINCE_CHOICES)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    representative = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    number = models.CharField(max_length=255, blank=True)
    date = models.DateField()
    mou = models.BooleanField()
    loi = models.BooleanField()
    signatory = models.CharField(max_length=255, blank=True)
    designation = models.CharField(max_length=255, blank=True)
    remarks = models.CharField(max_length=255, blank=True)
    
    def __str__(self) -> str:
        return f"[{self.batch} / {self.province}] {self.student_name} "