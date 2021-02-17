from django import forms
from django.utils import timezone

# Create your models here.
# https://www.geeksforgeeks.org/choicefield-django-forms/
toast_roast_choices = (
    ('1', 'toast'),
    ('2', 'roast')
)

class AddPostForm(forms.Form):
    text = forms.CharField(max_length=280)
    # likes = forms.IntegerField(default=0)
    # dislikes = forms.IntegerField(default=0)
    # time_created = forms.DateTimeField(default=timezone.now)
    toast_roast = forms.ChoiceField(choices=toast_roast_choices)
    