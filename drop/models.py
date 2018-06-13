import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Note(models.Model):
    NoteId = models.CharField(max_length=200)
    NoteContent = models.CharField(max_length=2000)
    #pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.NoteId
    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.pub_date <= now
