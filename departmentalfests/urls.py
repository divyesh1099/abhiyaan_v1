from django.urls import path
from . import views
app_name="departmentalfests"
urlpatterns=[
    path("", views.index, name="index"),
    path("<str:departmentalfest>", views.departmentalfest, name="departmentalfest"),
]