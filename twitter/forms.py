from django import forms
from django.forms import ModelForm
from .models import Tweet

# Creating the form class
class TweetForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']




