from django.urls import path

from . import views

urlpatterns = [
    # ex: /schedule/
    path('', views.home, name='home'),
    
    # ex: /schedule/1/student/
    path('<int:student_id>/student/', views.student, name='student'),
     
    # ex: /schedule/1/class_schedule/
    path('<int:student_id>/class_schedule/', views.class_schedule, name='class_schedule'),
    
    # student profile
    path('<int:student_id>/profile/', views.student_profile, name='profile'),
        
]