from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "days/index.html")

def day(request):
    return render(request, "days/day.html", {
        "day":"Name of Day"
    })