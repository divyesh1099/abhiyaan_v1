from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    sportlist=Sportlist.objects.all()
    return render(request, "sports/index.html", {
        "days": ["Clan", "Corporate", "Traditional"],
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })

def sport(request, sport):
    sportaa=Sportlist.objects.all()
    return render(request, "sports/sport.html", {
        "sport":sportaa,
        "days": ["Clan", "Corporate", "Traditional"],
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })