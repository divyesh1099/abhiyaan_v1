from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "sports/index.html")

def sport(request):
    return render(request, "sports/sport.html", {
        "sport":"Name of Sport"
    })