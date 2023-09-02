from django.db import models

# Create your models here.
from django.db import models
from embed_video.fields import EmbedVideoField

class Videos(models.Model):
    title=models.CharField(max_length=150)
    content=models.TextField()
    video = EmbedVideoField()

class Contact(models.Model):
    sno=models.AutoField(primary_key=True)   #serial number
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=60)
    phone=models.CharField(max_length=13)
    content=models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)