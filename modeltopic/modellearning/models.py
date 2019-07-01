from django.db import models

# Create your models here.
class Personname(models.Model):
     name = models.CharField(max_length=90)

     def __str__(self):
         return self.name

class Locationdata(models.Model):
    resident = models.ForeignKey(Personname,on_delete=models.CASCADE)
    location = models.CharField(max_length=90)

    def __str__(self):
        return self.location

class Jobdata(models.Model):
    employee=models.ForeignKey(Personname,on_delete=models.CASCADE)
    job=models.CharField(max_length=90)

    def __str__(self):
        return self.job
