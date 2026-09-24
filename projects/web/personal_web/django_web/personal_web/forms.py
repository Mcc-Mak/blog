"""Form classes for the personal_web application."""
from django.forms import ModelForm
from .models import *
from django import forms
# --- Blog post form ---
class BlogForm(ModelForm):
    class Meta:
        model = Model
        fields = ('title', 'content', 'img')  # '__all__'