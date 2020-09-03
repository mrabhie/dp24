from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=20,unique=True,blank=False)

class Webpage(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=20,unique=True,blank=False)
    url=models.URLField(max_length=100,unique=True,blank=False)

class Accessdetails(models.Model):
    webpage=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)

