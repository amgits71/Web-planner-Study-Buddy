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
    
class Category(models.Model): 
    name = models.CharField(max_length=100)
    class Meta:
    	verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    def __str__(self):
        return self.name  
    
class TodoList(models.Model):
	title = models.CharField(max_length=250)
	content = models.TextField(blank=True)
	created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) #дата создания
	due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) #до какой даты нужно было сделать дело
	category = models.ForeignKey(Category, default="general",on_delete=models.PROTECT) # foreignkey с помощью которой мы будем осуществлять связь с таблицей Категорий
	class Meta: #используем вспомогательный класс мета для сортировки наших дел
        ordering = ["-created"] #сортировка дел по времени их создания
	def __str__(self):
    	return self.title