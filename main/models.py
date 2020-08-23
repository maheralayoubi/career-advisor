from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from datetime import datetime

class User(AbstractUser):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    blocked = models.BooleanField(default=False)
    img = models.ImageField(upload_to='media')
    last_login = models.CharField(max_length = 30)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    username = models.CharField(default=email, max_length=200, unique=True)

class Instructor(User):
    field = models.CharField(max_length=100)
    catch_phrase = models.CharField(max_length = 200)
    intro_msg = models.CharField(max_length = 200)
    what_you_can_ask_for = models.CharField(max_length = 200)
    rating = models.FloatField(default=5)

class Student(User):
    major = models.CharField(max_length=100)
    level_of_study = models.CharField(max_length=200)

class Lesson(models.Model):
    title = models.CharField(max_length=50)
    # instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    # student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True)
    Date = models.DateTimeField(default=datetime.now())
    lesson_type = models.CharField(max_length=20)
    starting = models.CharField(max_length=20, default='None')
    ending = models.CharField(max_length=20, default='None')
