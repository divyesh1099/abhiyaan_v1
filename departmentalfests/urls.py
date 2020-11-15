from django.urls import path
from . import views
app_name="departmentalfests"
urlpatterns=[
    path("", views.index, name="index"),
    path("<str:department>", views.department, name="department"),
]