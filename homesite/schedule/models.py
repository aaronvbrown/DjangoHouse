from os import terminal_size
from typing import Optional
from django.db import models

# Create your models here.
#  TODO:  add a user field to the "student" model as a foreign key to the ones in the db.
class School(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name


class Teacher(models.Model):
    name_first = models.CharField(max_length=50)
    name_last = models.CharField(max_length=50)
    email = models.EmailField(default="", blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    contact = models.URLField(max_length=128, default="", null=True)
    title_preference = models.CharField(max_length=128, default="", null=True)
    # office_hours
    
    def __str__(self):
        whole_name = self.name_first + " " + self.name_last
        return whole_name


class Student(models.Model):
    name_first = models.CharField(max_length=50)
    name_last = models.CharField(max_length=50)
    email = models.EmailField(default="", blank=True)
    grade_level = models.IntegerField(default=0)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_first

class DaysOfTheWeek(models.Model):
    description = models.CharField(max_length=300)
    
    def __str__(self):
        return self.description

class Period(models.Model):
    period = models.IntegerField(default=1)
    time_start = models.TimeField
    time_end = models.TimeField
    days_in_session = models.ManyToManyField(DaysOfTheWeek)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.period)



class Course(models.Model):
    course_description = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    # period = models.ForeignKey(Period, on_delete=models.CASCADE) #Move to AcademicTerm model.

    def __str__(self):
        return self.course_description


class AcademicTerm(models.Model):
    school_year = models.CharField(max_length=300, default="2020-2021")
    school_term = models.CharField(max_length=300, default="TR1")
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        academic_term_name =  str(self.school_year) + " " + str(self.school) + " " + str(self.school_term)
        return academic_term_name

class ClassSchedule(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    academic_term = models.ForeignKey(AcademicTerm, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student) + " " + str(self.period) + " - " + str(self.course)

    def period(self):
        return self.period