from django.urls import path
from . import views

app_name = 'equation_solution'

urlpatterns = [
    path("", views.equation_solution, name="solution"),
]