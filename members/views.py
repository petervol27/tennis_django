from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Member


# Create your views here.
def members(request):
    members = Member.objects.all()
    context = {"members": members}
    return render(request, "members_page.html", context=context)


def member_details(request, id):
    member = Member.objects.get(id=id)
    context = {"member": member}
    return render(request, "member_details.html", context)
