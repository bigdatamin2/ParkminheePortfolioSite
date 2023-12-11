from django.db import models

class Board(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

class Certificate(models.Model):
    name = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)



