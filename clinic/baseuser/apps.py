from django.apps import AppConfig


class BaseUserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "clinic.baseuser"
