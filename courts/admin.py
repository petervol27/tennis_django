from django.contrib import admin
from .models import Court


# Register your models here.
class CourtAdmin(admin.ModelAdmin):
    list_display = ("name", "number", "is_occupied", "occupation_time")


admin.site.register(Court, CourtAdmin)
