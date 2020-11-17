from django.shortcuts import render
from .models import *
from departmentalfests.models import *
#-----------------------------------------------------------
departmentalfests=DepartmentalFest.objects.all()
departments=Department.objects.all()
#-----------------------------------------------------------
# Create your views here.
def index(request):
    days=Days.objects.all()[0]
    day=Day.objects.all()
    event=Event.objects.all()
    # return render(request, "days/index.html", {
    #     "days": ["Clan", "Corporate", "Traditional"],
    #     "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
    #     "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    # })
    return render(request, "days/index.html", {
        "days": days,
        "day":day,
        "departments": departments,
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })

def day(request, day):
    oday=Day.objects.all()
    days=Days.objects.all()
    tday=Day.objects.get(name=day)
    events=Event.objects.all()
    return render(request, "days/day.html", {
        "days": days,
        "day": oday,
        "tday":tday,
        "events": events,
        "departments": departments,
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })