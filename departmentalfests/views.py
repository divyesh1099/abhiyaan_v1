from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "departmentalfests/index.html", {
        "days": ["Clan", "Corporate", "Traditional"],
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })

def departmentalfest(request, departmentalfest):
    return render(request, "departmentalfests/departmentalfest.html", {
        "departmentalfest": departmentalfest,
        "days": ["Clan", "Corporate", "Traditional"],
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })