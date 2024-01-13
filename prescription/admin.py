from django.contrib import admin

# Register your models here.
from .models import Prescription

# from .models import Drug

admin.site.register(Prescription)
# admin.site.register(Drug)
