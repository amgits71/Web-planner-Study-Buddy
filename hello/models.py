import sqlite3
from django.utils import timezone
from django.db import models

class Users(models.Model):
    genders = (
        ("Мужчина", "Male"),
        ("Женщина", "Female")
    )
    answer = (
        ("Да", "yes"),
        ("Нет", "no")
    )
    nickname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    age = models.IntegerField(default = 0)
    gender = models.CharField(max_length = 50, choices = genders)
    study = models.CharField(max_length = 50, choices = answer)
    work = models.CharField(max_length = 50, choices = answer)
    
