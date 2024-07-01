from django.db import models

class Music(models.Model):
    Name = models.AutoField(primary_key=True)
    Movie = models.CharField(max_length=100)
    Singer= models.CharField(max_length=100)
    Lyricist = models.CharField(max_length=100)
