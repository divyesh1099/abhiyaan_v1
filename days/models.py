from django.db import models


# Create your models here.
class Event(models.Model):
    name           =  models.CharField(max_length=64)
    image          =  models.ImageField(blank=True)
    description    =  models.TextField(blank=True)
    eventhead      =  models.CharField(max_length=64)
    rules          =  models.TextField(blank=True)
    trialimage     =  models.ImageField(blank=True)


    def __str__(self):
        return self.name

class Day(models.Model):
    name        =  models.CharField(max_length=64)
    imageOne    =  models.ImageField(blank=True)
    imageTwo    =  models.ImageField(blank=True)
    imageThree  =  models.ImageField(blank=True)
    description =  models.TextField(blank=True)
    events      =  models.ManyToManyField(Event, blank=True, related_name="eventsofday")


    def __str__(self):
        return self.name
    

class Days(models.Model):
    imageOne   =  models.ImageField(blank=True)
    imageTwo   =  models.ImageField(blank=True)
    imageThree =  models.ImageField(blank=True)
    description=  models.TextField(blank=True)
    day        =  models.ManyToManyField(Day, blank=True, related_name="dayofdays")


    def __str__(self):
        return 'Days'