from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# jwt
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .api_router import router

schema_view = get_schema_view(
    openapi.Info(
        title="clinic API",
        default_version="v24.2.13",
        description="These api sets are developed for a medical website, which you can read in more detail below",
        contact=openapi.Contact(email="More.amani@yahoo.com"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("api/auth/", include("rest_framework.urls")),
    path("api/v2/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v2/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]


urlpatterns += [
    path("api/admin/", admin.site.urls),
    path("api/", include(router.urls)),
    # path("api/doctor/", include("doctor.urls")),
    # path("api/exercise/", include("exercise.urls")),
    # path("api/patient/", include("patient.urls")),
    # path("api/prescription/", include("prescription.urls")),
    # path("api/reports/", include("reports.urls")),
    # path("session/", include("session.urls")),
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

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
# Add a URL pattern for serving video files
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
