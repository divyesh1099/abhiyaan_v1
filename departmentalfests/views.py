from django.shortcuts import render
from days.models import *
from .models import *
#---------------------------------------------------
days=Days.objects.all()[0]
day=Day.objects.all()
departmentalfests=DepartmentalFest.objects.all()[0]
departments=Department.objects.all()
events=Event.objects.all()
#---------------------------------------------------

# Create your views here.
def index(request):
    return render(request, "departmentalfests/index.html", {
        "days": days,
        "day":day,
        "departments": departments,
        "departmentalfests": departmentalfests,
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    }) 

def department(request, department):
    tdepartment=Department.objects.get(name=department)
    return render(request, "departmentalfests/department.html", {
        "days": days,
        "day": day,
        "departments": departments,
        "tdepartment": tdepartment,
        "events": events,
        "departmentalfests": departmentalfests,
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })