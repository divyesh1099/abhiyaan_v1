from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "maineventsdaythree/index.html")

def maineventsdaythree(request):
    return render(request, "maineventsdaythree/maineventsdaythree.html", {
        "maineventsdaythree":"Name Of Events"
    })