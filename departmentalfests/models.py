from django.db import models

# Create your models here.
class Event(models.Model):
    name        =   models.CharField(max_length=64)
    image       =   models.CharField(max_length=1000)
    description =   models.CharField(max_length=1000)
    procedure   =   models.CharField(max_length=1000)

    def __str__(self):
        return name
    
class Department(models.Model):
    name        =   models.CharField(max_length=64)
    description =   models.CharField(max_length=1000)
    imageOne    =   models.CharField(max_length=1000)
    imageTwo    =   models.CharField(max_length=1000)
    imageThree  =   models.CharField(max_length=1000)
    events      =   models.ManyToManyField(Event, related_name="eventofdepartment", blank=True)

    def __str__(self):
        return name

class DepartmentalFest(models.Model):
    imageOne    =   models.CharField(max_length=1000)
    imageTwo    =   models.CharField(max_length=1000)
    imageThree  =   models.CharField(max_length=1000)
    description =   models.CharField(max_length=1000)
    department  =   models.ManyToManyField(Department, related_name="departmentofdepartmentalfests", blank=True)
