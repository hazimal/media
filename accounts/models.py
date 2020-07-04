from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    mod_type = models.BooleanField(default=True)
    add_date = models.DateTimeField(auto_created=True)


    def __str__(self):
        return self.name + " " + self.last_name


class Student(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.BooleanField(default=True)
    add_date = models.DateTimeField(auto_created=True)


    def __str__(self):
        return self.name + " " + self.last_name
