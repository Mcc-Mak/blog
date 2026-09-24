"""Admin configuration for personal_web."""
from django.contrib import admin
from .models import Model
# --- Register models with the Django admin ---
admin.site.register(Model)
