from django.shortcuts import render, redirect
from .models import Court
from members.models import Member

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


def occupy_court(id):
    court = Court.objects.get(id=id)
    court.occupy()
    court.save()
    return redirect("courts")


def end_court_occupation(id):
    court = Court.objects.get(id=id)
    court.end_occupation()
    court.save()
    return redirect("courts")


def reservation(request, id):
    all_members = Member.objects.all()
    available_members = []
    for member in all_members:
        if not member.court:
            available_members.append(member)
    chosen_court = Court.objects.get(id=id)
    context = {"court": chosen_court, "available_members": available_members}
    if request.method == "POST":
        member1 = request.POST.get("member1")
        member2 = request.POST.get("member2")
        return redirect("courts")
    else:
        return render(request, "court_order.html", context)
