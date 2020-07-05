from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
# Create your models here.
class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter().filter(publish__lte=timezone.now())

class Course(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

    objects = PostManager()


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(settings.AUTH_USER_MODEL, max_length=250)
    password = models.CharField(max_length=512)#, widget=forms.PasswordInput)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    mod_type = models.BooleanField(default=True)
    add_date = models.DateTimeField(auto_created=True)
    # class Meta:
    #     model = User

    def __str__(self):
        return self.name + " " + self.last_name


class Student(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(settings.AUTH_USER_MODEL, max_length=250)#, widget=forms.EmailField)
    password = models.CharField(max_length=512)#, widget=forms.PasswordInput)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.BooleanField(default=True)
    add_date = models.DateTimeField(auto_created=True)


    objects = PostManager()


    def __str__(self):
        return self.name + " " + self.last_name
