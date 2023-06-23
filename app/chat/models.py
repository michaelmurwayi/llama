from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255)


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now=True)
    