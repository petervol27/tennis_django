from django.shortcuts import render, redirect
from .models import Court


# Create your views here.


def courts(request):
    courts = Court.objects.all()
    context = {"courts": courts}
    return render(request, "courts_page.html", context=context)


def court_details(request, id):
    court = Court.objects.get(id=id)
    members = court.members.all()
    context = {"court": court, "members": members}
    return render(request, "court_details.html", context)


def occupy_court(request, id):
    court = Court.objects.get(id=id)
    court.occupy()
    court.save()
    return redirect("court_details", id=id)


def end_court_occupation(request, id):
    court = Court.objects.get(id=id)
    court.end_occupation()
    court.save()
    return redirect("court_details", id=id)
