from django.forms import ModelForm
from .models import *
from django import forms


class BlogForm(ModelForm):
    class Meta:
        model = Model
        fields =('title','content','img') #'__all__'
        