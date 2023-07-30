from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# creating student user database table
class StudentUser(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    mobileNo =models.CharField(max_length=10,null=False)
    profileImage =models.FileField(null=False)
    gender =models.CharField(max_length=10,null=False)
    type =models.CharField(max_length=15,null=False)

    def __str__(self):
        return self.user.username

# recruiter class for table

class RecruiterReg(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobileNo =models.CharField(max_length=10,null=False)
    profileImage =models.FileField(null=False)
    gender =models.CharField(max_length=10,null=False)
    company =models.CharField(max_length=90,null=False)
    status =models.CharField(max_length=20,null=False)
    type =models.CharField(max_length=15,null=False)

    def __str__(self):
        return self.user.username


# Model for jobs
class Job(models.Model):
    recruiter = models.ForeignKey(RecruiterReg,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,null=False)
    image = models.FileField()
    company = models.CharField(max_length=50,null=False)
    salary = models.CharField(max_length=10, null=True)
    location = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=3000,null=True)
    joburl = models.URLField(max_length=1000,null=False,default='NULL')
    creationdate = models.DateField()

    def __str__(self):
        return self.title