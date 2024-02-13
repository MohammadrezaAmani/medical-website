from django.contrib import admin

from .models import CustomUser, Doctor, PateintDoctor, Patient

admin.site.site_header = "Clinic Admin"

admin.site.register(CustomUser)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(PateintDoctor)
