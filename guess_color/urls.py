from django.urls import path
from . import views

app_name = 'guess_color'

urlpatterns = [
    path("", views.guess_color, name="guess"),
]