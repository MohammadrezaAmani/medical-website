from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = []


schema_view = get_schema_view(
    openapi.Info(
        title="ThritaTech API",
        default_version="v3.2.6",
        description="Nothing",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="More.amani@yahoo.com"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("doctor/", include("doctor.urls")),
    path("exercise/", include("exercise.urls")),
    path("patient/", include("patient.urls")),
    path("prescription/", include("prescription.urls")),
    path("reports/", include("reports.urls")),
    path("session/", include("session.urls")),
    # path("prescription/", include("session.urls")),
    # Swagger documentation URL
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
