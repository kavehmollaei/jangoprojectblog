from django.contrib.admin.sites import site
from django.db import models
from django.db.models.fields import IntegerField
from django.utils import timezone


# Create your models here.
class Topic(models.Model):
    """ Topic Models"""
    Low = 1
    High = 2
    
    Hours = (
        (Low,"One"),
        (High,"Two"),
    )
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    hours_topic = models.IntegerField(default=0,choices=Hours)
    Upload_Image_For_Topic = models.ImageField(null=True,blank=True,max_length=100)
    def __str__(self) -> str:
        return self.text



class Entry(models.Model):
    """Something specific learned aboute a topic"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    title = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"


    def __str__(self) -> str:
        return f"{self.title[:50]}..."






class Person(models.Model):
    sex_choices = (
        ("M","Male"),
        ("F","Female"),
    )

    status_choices = (
        ("d","Draf"),
        ("p","Published")
    )
    
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    sex = models.CharField(max_length=4,choices=sex_choices)
    publish_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1,choices=status_choices)
    def __str__(self) -> str:
        return self.family


       