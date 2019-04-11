from django import forms
from django.forms import ModelForm
from .models import Tweet

# Creating the form class
class TweetForm(ModelForm):
    content = forms.CharField(label='', 
    widget=forms.Textarea(attrs={'placeholder': "Tweet here", "class":"form-control"}))
    class Meta:
        model = Tweet
        fields = ['content']




