from django import forms
from django.forms import ModelForm
from .models import Tweet

# Creating the form class
class TweetForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ['user','content']

# def clean_content(self, *args, **kwargs):
#     content = self.cleaned_data.get("content")
#     if content == "abc":
#         raise forms.ValidationError("Cannot be ABC")
#     return content



