from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from course.models import CourseInstance

@login_required
def home(request):
    return render( request, 'account/student_home.html' )

def my_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('courses')
        else:
            return redirect('courses')
    else:
        return redirect('courses')

def my_logout(request):
    logout(request)
    return redirect('courses')