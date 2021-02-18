from django import forms
from django.utils import timezone

# Create your models here.
# https://www.geeksforgeeks.org/choicefield-django-forms/
boast_roast_choices = (
    ('1', 'boast'),
    ('2', 'roast')
)

class AddPostForm(forms.Form):
    text = forms.CharField(max_length=280)
    choose = forms.ChoiceField(choices=boast_roast_choices)
    