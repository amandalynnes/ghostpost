from django.db import models
from django.utils import timezone

# Create your models here.
# https://stackoverflow.com/questions/8077840/choicefield-in-django-model

class PostItem(models.Model):
    boast_roast_choices = (
    (True, 'boast'),
    (False, 'roast')
    )
    text = models.CharField(max_length=280)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    time_created = models.DateTimeField(default=timezone.now())
    choose = models.BooleanField(choices=boast_roast_choices)



    def __str__(self):
        return self.text

    def score(self):
        score = self.likes - self.dislikes
        return score