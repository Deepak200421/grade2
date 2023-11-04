from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView

from .models import Student, Course, Grade
from .forms import StudentForm, CourseForm, GradeForm

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm()
    return render(request, 'grades/add_student.html', {'form': form})


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CourseForm()
    return render(request, 'grades/add_course.html', {'form': form})

def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = GradeForm()
    return render(request, 'grades/add_grade.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'grades/student_list.html', {'students': students})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'grades/course_list.html', {'courses': courses})

def grade_list(request):
    grades = Grade.objects.all()
    return render(request, 'grades/grade_list.html', {'grades': grades})


from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, 'grades/register.html', {'title': 'Home'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} created Successfully')
            return redirect('grades-base')
    else:
        form = UserRegisterForm()
    return render(request, 'grades/register.html', {'form': form})
@login_required
def profile(request):
    return render(request, 'grades/profile.html')


class ContactListView(ListView):
    paginate_by = 4
    model = Grade

def list(request):
    person_list = Grade.objects.all()
    paginator = Paginator(person_list,4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'grades/list.html', {"page_obj": page_obj})
