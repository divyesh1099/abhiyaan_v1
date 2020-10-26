from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "maineventsdayone/index.html", {
        "days": ["Clan", "Corporate", "Traditional"],
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })

def maineventsdayone(request):
    return render(request, "maineventsdayone/maineventsdayone.html", {
        "maineventsdayone":"Name Of Events"
    })