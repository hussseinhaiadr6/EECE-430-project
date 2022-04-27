from django.db import models
from datetime import *
class Client(models.Model):
    Male = 'M'
    Female = 'F'
    Gender = [
    ('M', 'Male'),
    ('F', 'Female'),
]
    Manager = 'M'
    Client = 'C'
    Role = [
    ('M', 'Manager'),
    ('C', 'Client'),
]
   
    Client_name = models.CharField(max_length=30)
    Client_pass= models.CharField(max_length=30)
    Client_email = models.EmailField(max_length=60)
    Client_phone = models.IntegerField(default=0)
    Client_address= models.CharField(max_length=255)
    Client_gender=models.CharField(
        max_length=1,
        choices=Gender,
        default=Male,
    )
    Client_age=models.IntegerField()
    Client_role=models.CharField(
        max_length=1,
        choices=Role,
        default=Client,
    )
    def __str__(self):
        ret = self.Client_name + ',' + self.Client_email
        return ret
class Instructor(models.Model):
    Male = 'M'
    Female = 'F'
    Gender = [
    ('M', 'Male'),
    ('F', 'Female'),
]
   
    Instructor_name = models.CharField(max_length=30)
    Instructor_email = models.CharField(max_length=30)
    Instructor_phone = models.IntegerField(default=0)
    Instructor_age=models.IntegerField()
    Instructor_photo=models.CharField(max_length=100)
    Instructor_specialty=models.CharField(max_length=100)
    Instructor_gender=models.CharField(
        max_length=1,
        choices=Gender,
        default=Male,
    )
    def __str__(self):
        ret = self.Instructor_name + ',' + self.Instructor_email
        return ret
    
class Class(models.Model):
  Class_id=models.CharField(primary_key=True,max_length=2)
  Class_name=models.CharField(max_length=30)
  Class_instructor=models.ForeignKey(Instructor,on_delete=models.CASCADE)
  Class_capacity=models.IntegerField(default=20)
  def __str__(self):
        ret = self.Class_id + ',' + self.Class_name
        return ret

class Membership(models.Model):
    Basic = 'B'
    Standard = 'S'
    Premium = 'P'
    membership = [
    ('B', 'Basic'),
    ('S', 'Standard'),
    ('P', 'Premium'),
]
    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    initial = models.DateField( default=date.today())
    expired= models.DateField()
    membershipType=models.CharField(
        max_length=1,
        choices=membership,
        default=Standard,
    )
    def __str__(self):
        ret = self.client.Client_email + ',' + self.membershipType
        return ret
class Reservation(models.Model):

    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    class_id=models.CharField(max_length=2)
    def __str__(self):
        ret = self.client.Client_email + ',' + self.class_id
        return ret
 


class applicant(models.Model):
    idofapp = models.CharField(max_length=255,default=0)
    name = models.CharField(max_length=255,default=0)
    email = models.CharField(max_length=255,default=0)
    country = models.CharField(max_length=255,default=0)
    currentstate = models.CharField(max_length=255,default=0)
    phonenumber =  models.IntegerField(default=0)
    submition_date = models.DateTimeField(auto_now_add=True,null=True)
    selectedjobid = models.CharField(max_length=255,default=0)

class jobs(models.Model):
    idofjob = models.CharField(max_length=255,default=0)
    position = models.CharField(max_length=255,default=0)
    location = models.CharField(max_length=255,default=0)
    salary = models.CharField(max_length=255,default=0)
    jobschedule = models.CharField(max_length=255,default=0)