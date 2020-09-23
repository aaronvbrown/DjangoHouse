from django.contrib import admin

# Register your models here.
from .models import School, Teacher, Student, Course, Period

admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Period)
