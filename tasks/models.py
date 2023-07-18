from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200) # No particular reason for the max_length
    completed = models.BooleanField(default=False)
    

class DeletedTask(models.Model):
    title = models.CharField(max_length=200) # No particular reason for the max_length
