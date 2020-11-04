from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    sportlist=Sportlist.objects.all()
    print(sportlist[0].sports)
    return render(request, "sports/index.html", {
        "days": ["Clan", "Corporate", "Traditional"],
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })

def sport(request, sport):
    sportaa=Sportlist.objects.all()
    print(sportaa.name)
    return render(request, "sports/sport.html", {
        "sport":sport,
        "days": ["Clan", "Corporate", "Traditional"],
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })