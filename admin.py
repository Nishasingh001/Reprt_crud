from django.contrib import admin
from .models import (
   DailyReport
)


@admin.register(DailyReport)
class Useradmin(admin.ModelAdmin):
    list_display=("id","name", "email","assigned_work","completed","pending"         
    )
