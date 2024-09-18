from django.db import models
from courts.models import Court


# Create your models here.
class Trainer(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=13)
    court = models.ForeignKey(
        Court, on_delete=models.SET_NULL, null=True, related_name="trainers"
    )

    def __str__(self):
        return f"{self.fname} {self.lname}"
