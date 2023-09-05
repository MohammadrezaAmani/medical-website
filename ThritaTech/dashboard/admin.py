from django.contrib import admin

# Register your models here.
from .models import Calendar, CalendarItem

admin.site.register(Calendar)
admin.site.register(CalendarItem)