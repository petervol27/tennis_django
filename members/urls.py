from django.urls import path
from . import views

urlpatterns = [
    path("", views.members, name="members"),
    path("member_details/<int:id>", views.member_details, name="member_details"),
]
