from django.db import models
from django.utils import timezone

# Create your models here.

class PostItem(models.Model):
    text = models.CharField(max_length=280)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    time_created = models.DateTimeField(default=timezone.now())
    toast_roast = models.BooleanField()

    def __str__(self):
        return f"{self.text}"