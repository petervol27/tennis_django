from django.urls import path
from . import views

urlpatterns = [
    path("", views.trainers, name="trainers"),
    path("trainer_details/<int:id>", views.trainer_details, name="trainer_details"),
]
