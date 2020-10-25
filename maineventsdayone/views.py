from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "maineventsdayone/index.html")

def maineventsdayone(request):
    return render(request, "maineventsdayone/maineventsdayone.html", {
        "maineventsdayone":"Name Of Events"
    })