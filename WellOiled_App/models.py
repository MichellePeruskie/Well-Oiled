from __future__ import unicode_literals
from django.db import models
import re

# from WellOiled.admin import admin
# from object_attachments.admin import ObjectAttachmentInline



class RegMgr(models.Manager):
    def basic_validator(self, PostData):
        errors= {}
        if len (PostData['f_n']) < 2:
            errors["first_name"] = "First name and/or last name must be at least two characters long."
        if len (PostData['l_n']) < 2:
            errors["last_name"] = "First name and/or last name must be at least two characters long."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(PostData['email']):              
            errors['email'] = ("Invalid email address!")
        if len(PostData['pw']) < 8:
            errors["pw"]= "Password must be at least 8 characters long."
        if PostData['pw'] != PostData['conf_pw']: 
            errors['conf_pw'] = 'Passwords do not match'
        return errors

class Register(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    company= models.CharField(max_length=255)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegMgr()

class Login(models.Model):
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegMgr()

# class EmpMgr(models.Manager):
#     def employee_validator(self, PostData):
#         errors= {}
#         if len (PostData['e_f_n']) < 2:
#             errors["first_name"] = "First name and/or last name must be at least two characters long."
#         if len (PostData['e_l_n']) < 2:
#             errors["last_name"] = "First name and/or last name must be at least two characters long."
#         EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#         if not EMAIL_REGEX.match(PostData['e_c_email']):              
#             errors['e_c_email'] = ("Invalid email address!")
#         if len(PostData['e_pw']) < 8:
#             errors["e_pw"]= "Password must be at least 8 characters long."
#         if PostData['e_pw'] != PostData['e_conf_pw']: 
#             errors['e_conf_pw'] = 'Passwords do not match'
#         return errors

class Employee (models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_email = models.CharField(max_length=255)
    # company = models.ForeignKey(Register, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    comp_level= models.CharField(max_length=8)
    zipcode=models.CharField(max_length=5)
    initial_password=models.CharField(max_length=45)
    photo=models.CharField(null=True, blank=True, max_length=255)
    # smltap = models.BooleanField(default=False)
    # lrgtap = models.BooleanField(default=False)
    # smlcomp = models.BooleanField(default=False)
    # lrgcomp = models.BooleanField(default=False)
    # iso = models.BooleanField(default=False)
    # highp = models.BooleanField(default=False)
    # angle = models.BooleanField(default=False)
    # created_at = models.DateTimeField(null=True, blank=True,auto_now_add=True)
    # updated_at = models.DateTimeField(null=True, blank=True,auto_now=True)
    # objects=EmpMgr()


class JobMgr(models.Manager):
    def job_validator(self, PostData):
        errors= {}
        if len (PostData['company']) < 2:
            errors["first_name"] = "Company name must be at least two characters long."
        #need validiation to ensure employee is not scheduled for two thigns at once 
        #and that there is a day inbetwen scheduling them. 
        return errors

class JobParameters(models.Model):
    employee= models.ManyToManyField(Employee, related_name="jobparameters")
    tap= models.BooleanField(default=False)
    plug= models.BooleanField(default=False)
    isolate= models.BooleanField(default=False)
    psi= models.CharField(max_length=5)
    size= models.CharField(max_length=20)
    angle= models.BooleanField(default=False)
    company = models.CharField(max_length=255)
    jobstart= models.DateField()
    jobend= models.DateField()
    location=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=JobMgr()

# class Documentation(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     # https://pypi.org/project/django-document-library/