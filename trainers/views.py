from django.shortcuts import render
from .models import Trainer


# Create your views here.
def trainers(request):
    trainers = Trainer.objects.all().values()
    context = {"trainers": trainers}
    return render(request, "trainers_page.html", context=context)


def trainer_details(request, id):
    trainer = Trainer.objects.get(id=id)
    context = {"trainer": trainer}
    return render(request, "trainer_details.html", context)
