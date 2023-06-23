from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, unique=True)


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
