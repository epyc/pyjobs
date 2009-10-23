from django.db import models

# Create your models here.
class Job(models.Model):
  title = models.CharField(max_length=200)
  location = models.CharField(max_length=40)
  date_added = models.DateTimeField('date added')
  date_expires = models.DateTimeField('date expires', null=True, blank=True)
  content = models.TextField('content', blank=True)


  
   
