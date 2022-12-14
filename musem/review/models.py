from django.db import models


class Message(models.Model):
    author_name = models.CharField(max_length=60)
    text = models.TextField()
