from .models import Period, Student, ClassSchedule
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

# home page for the app.  Should display Student Names.
def home(request):
    student_list = Student.objects.order_by('name_last', 'name_first')
    template = loader.get_template('schedule/home.html')
    context = {
        'student_list': student_list
    }
    return render(request, 'schedule/home.html', context)


# home page for the student.  Should display apps available to the student.
def student(request, student_id):
    student_to_load = Student.objects.filter(id=student_id)
    template = loader.get_template('schedule/student.html')
    context = { 
        'student_to_load': student_to_load
    }
    return render(request, 'schedule/student.html', context)
    
# class schedule
def class_schedule(request, student_id):
    # response = "You're looking at %s's schedule."
    # return HttpResponse(response % student_id)
    classes_scheduled = ClassSchedule.objects.filter(student=student_id).order_by('period')
    template = loader.get_template('schedule/class_schedule.html')
    context = { 
        'classes_scheduled': classes_scheduled
    }
    return render(request, 'schedule/class_schedule.html', context)

# student profile
def student_profile(request, student_id):
    response = "%s's Profile"
    return HttpResponse(response % student_id)

