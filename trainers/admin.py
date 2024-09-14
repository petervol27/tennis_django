from django.contrib import admin
from .models import Trainer


# Register your models here.
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("fname", "lname", "email", "phone")


admin.site.register(Trainer, TrainerAdmin)
