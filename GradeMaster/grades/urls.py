from django.urls import path
from . import views

urlpatterns = [
    path('add_student', views.add_student, name='add_student'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_grade/', views.add_grade, name='add_grade'),
    path('student_list/', views.student_list, name='student_list'),
    path('course_list/', views.course_list, name='course_list'),
    path('grade_list/', views.grade_list, name='grade_list'),
    path('', views.profile, name="grades/profile"),
    path('list', views.list, name="grades/list"),
]
