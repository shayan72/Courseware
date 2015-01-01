from django.shortcuts import render

from django.shortcuts import render, redirect

# Create your views here.

def courses(request):
    return render(request, 'course/courses.html')