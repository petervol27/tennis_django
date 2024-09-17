from django.db import models
from courts.models import Court
from trainers.models import Trainer
from django.utils import timezone


# Create your models here.


class Member(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    join_date = models.DateField(max_length=254)
    court = models.ForeignKey(
        Court, on_delete=models.SET_NULL, null=True, blank=True, related_name="members"
    )
    trainer = models.ForeignKey(
        Trainer, on_delete=models.SET_NULL, null=True, related_name="trainees"
    )

    def __str__(self):
        return f"{self.fname} {self.lname} "

    def save_court_to_member(self, court):
        self.court = court
