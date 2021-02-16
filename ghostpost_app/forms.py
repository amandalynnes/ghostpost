from django import forms
from django.utils import timezone

# Create your models here.

class AddPostForm(forms.Form):
    text = forms.CharField(max_length=280)
    likes = forms.IntegerField()
    dislikes = forms.IntegerField()
    time_created = forms.DateTimeField()
    toast_roast = forms.BooleanField()
