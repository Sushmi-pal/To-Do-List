from django.db import models

# Create your models here.
class Todo(models.Model):
    message=models.CharField(max_length=50)