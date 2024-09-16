from django.urls import path
from . import views


urlpatterns = [
    path("", views.courts, name="courts"),
    path("court_details/<int:id>", views.court_details, name="court_details"),
    path("court_details/<int:id>/reservation", views.reservation, name="reservation"),
    path(
        "court_detail/<int:id>/end_reservation",
        views.end_reservation,
        name="end_reservation",
    ),
]
