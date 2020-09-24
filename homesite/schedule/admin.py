from django.contrib import admin

# Register your models here.
from .models import AcademicTerm, DaysOfTheWeek, School, Teacher, Student, Course, Period, ClassSchedule

admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Period)
admin.site.register(DaysOfTheWeek)
admin.site.register(AcademicTerm)
admin.site.register(ClassSchedule)