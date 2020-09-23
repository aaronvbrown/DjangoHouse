from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=250)


class Teacher(models.Model):
    name_first = models.CharField(max_length=50)
    name_last = models.CharField(max_length=50)
    email = models.EmailField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)


class Student(models.Model):
    name_first = models.CharField(max_length=50)
    name_last = models.CharField(max_length=50)
    email = models.EmailField()
    grade_level = models.IntegerField(default=0)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

day_of_the_week = (
        (1, "Monday"),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday")
    )

class Period(models.Model):
    period = models.IntegerField
    time_start = models.TimeField
    time_end = models.TimeField
    days_in_session = models.CharField(max_length = 15, choices = day_of_the_week)
    school = models.ForeignKey(School, on_delete=models.CASCADE)



class Course(models.Model):
    course_description = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
