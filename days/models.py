from django.db import models

# Create your models here.
class Event(models.Model):
    name           =  models.CharField(max_length=64)
    image          =  models.CharField(max_length=1000)
    description    =  models.CharField(max_length=1000)
    eventhead      =  models.CharField(max_length=64)
    rules          =  models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Day(models.Model):
    name           =  models.CharField(max_length=64)
    imageOne    =  models.CharField(max_length=1000)
    imageTwo    =  models.CharField(max_length=1000)
    imageThree  =  models.CharField(max_length=1000)
    description    =  models.CharField(max_length=64)
    events         =  models.ManyToManyField(Event, blank=True, related_name="eventsofday")

    def __str__(self):
        return self.name
    

class Days(models.Model):
    imageOne   =  models.CharField(max_length=1000)
    imageTwo   =  models.CharField(max_length=1000)
    imageThree =  models.CharField(max_length=1000)
    description    =  models.CharField(max_length=1000)
    day            =  models.ManyToManyField(Day, blank=True, related_name="dayofdays")

    def __str__(self):
        return 'Days'