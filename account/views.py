from django.shortcuts import render, redirect

from course.models import CourseInstance
# Create your views here.

def home(request, username):
    return render( request, 'account/student_home.html' )
