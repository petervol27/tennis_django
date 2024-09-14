from django.db import models
from django.utils import timezone


# Create your models here.
class Court(models.Model):
    name = models.CharField(max_length=100)
    number = models.PositiveIntegerField(unique=True)
    is_occupied = models.BooleanField(default=False)
    occupation_time = models.DateTimeField(null=True, blank=True)
    

    def __str__(self):
        return self.name

    def occupy(self):
        self.is_occupied = True
        self.occupation_time = timezone.now()

    def end_occupation(self):
        self.is_occupied = False
        self.occupation_time = None
