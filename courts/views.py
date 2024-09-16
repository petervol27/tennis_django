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


def end_reservation(request, id):
    court = Court.objects.get(id=id)
    members = court.members.all()
    for member in members:
        member.court = None
        member.save()
    court.end_reserve()
    court.save()
    return redirect("courts")


def reservation(request, id):
    all_members = Member.objects.all()
    available_members = [member for member in all_members if not member.court]
    chosen_court = Court.objects.get(id=id)
    context = {"court": chosen_court, "available_members": available_members}
    if request.method == "POST":
        member1_id = request.POST.get("member1")
        member2_id = request.POST.get("member2")
        print(member1_id)
        print(member2_id)
        if member1_id == member2_id or member1_id == "" or member2_id == "":
            error = "Has to be two different members or not an empty option!"
            print("nope")
            context = {
                "court": chosen_court,
                "available_members": available_members,
                "errortxt": error,
            }
            return render(request, "court_order.html", context)
        else:
            print("yes")
            member1 = Member.objects.get(id=member1_id)
            member2 = Member.objects.get(id=member2_id)
            member1.court = chosen_court
            member2.court = chosen_court
            chosen_court.reserve()
            member1.save()
            member2.save()
            chosen_court.save()
            return redirect("courts")
    else:
        return render(request, "court_order.html", context)
