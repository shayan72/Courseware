from django.shortcuts import render, redirect

from course.models import CourseInstance

# Create your views here.

def courses(request):
    return render(request, 'course/courses.html')

def courses_of_term(request, course_year_1, course_year_2, term ):

    SEMESTER = 'SU'
    if( term == '1' ):
        SEMESTER = 'FA'
    elif( term == '2' ):
        SEMESTER = 'SP'

    course_instance_list = CourseInstance.objects.filter(term__year=course_year_1).filter(term__semester=SEMESTER)

    return render(request, 'course/courses.html', {'course_instance_list':course_instance_list})

def course_page(request, course_year_1, course_year_2, term, course_num, course_group ):
    return render(request, 'course/course_page.html' )

def course_syllabus(request, course_year_1, course_year_2, term, course_num, course_group ):
    return render(request, 'course/course_syllabus.html' )

def course_calendar(request, course_year_1, course_year_2, term, course_num, course_group ):
    return render(request, 'course/course_calendar.html' )

def course_assignments(request, course_year_1, course_year_2, term, course_num, course_group ):
    return render(request, 'course/course_assignments.html' )

def course_grades(request, course_year_1, course_year_2, term, course_num, course_group ):
    return render(request, 'course/course_grades.html' )

def course_videolectures(request, course_year_1, course_year_2, term, course_num, course_group ):
    return render(request, 'course/course_videolectures.html' )

def course_resources(request, course_year_1, course_year_2, term, course_num, course_group ):
    return render(request, 'course/course_resources.html' )

def course_forum(request, course_year_1, course_year_2, term, course_num, course_group ):
    return render(request, 'course/course_forum.html' )