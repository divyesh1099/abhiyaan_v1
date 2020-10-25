from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "departmentalfests/index.html")

def departmentalfest(request):
    return render(request, "departmentalfests/departmentalfest.html", {
        "departmentalfest":"NAME OF DEPARTMENT"
    })