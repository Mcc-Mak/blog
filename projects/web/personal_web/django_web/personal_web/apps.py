"""App configuration for the personal_web Django application."""
from django.apps import AppConfig


class PersonalWebConfig(AppConfig):
    # Default primary key field type for auto-generated fields
    default_auto_field = "django.db.models.BigAutoField"
    name = "personal_web"
