from django.urls import path
from . import views
app_name="days"
urlpatterns=[
    path("", views.index, name="index"),
    path("<str:day>", views.day, name="day"),
]