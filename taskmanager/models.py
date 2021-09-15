from django.db import models

# Create your models here.

class Person(models.Model):
    username = models.TextField()
    password = models.TextField()
    firstname = models.TextField()
    lastname = models.TextField()
    loggedin = models.TextField(default='False')

class Task(models.Model):
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()