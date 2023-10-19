from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("doctor/", include("doctor.urls")),
    path("exercise/", include("exercise.urls")),
    path("patient/", include("patient.urls")),
    path("prescription/", include("prescription.urls")),
    path("reports", include("reports.urls")),
]
