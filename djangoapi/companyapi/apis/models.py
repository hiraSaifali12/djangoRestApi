
from django.db import models
#from  .import Company, Employee
#from django.apps import apps



# Create your models here.

#creating Company model
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100, choices=(('IT','IT'),
                                                   ('Non IT','Non IT'),
                                                   ('Mobile Phone','Mobile Phone')
                                                   ))
    
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
          return self.name + "--" + self.location 

    #creating employee
class Employee(models.Model):
       name=models.CharField(max_length=100)
       email=models.CharField(max_length=50)
       address=models.CharField(max_length=100)
       phone=models.CharField(max_length=10)
       about=models.TextField()
       position=models.CharField(max_length=50,choices=(('mg','mg'),
                                            ('tl','tl'),
                                            ('sd','sd'),
                                            ))
       company=models.ForeignKey(Company,on_delete=models.CASCADE)