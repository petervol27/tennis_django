from django.db import models
from courts.models import Court
from django.utils import timezone


# Create your models here.


class Member(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    join_date = models.DateField(max_length=254)
    # trainer = models.ForeignKey(
    #     Trainer, on_delete=models.SET_NULL, null=True, related_name="members"
    # )
    court = models.ForeignKey(Court, on_delete=models.SET_NULL,null=True,related_name="members")

    def __str__(self):
        return f"{self.fname} {self.lname} "
