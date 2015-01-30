from django.shortcuts import render

from course.models import CourseInstance
from course.models import Syllabus
from course.models import Calendar
from course.models import Assignment
from course.models import Grade
from course.models import Resource
from course.models import Topic

# Create your views here.

def manage_home(request, course_year_1, course_year_2, term, course_num, course_group):
    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)

    variables = {'course_instance': course_instance}

    return render(request, 'course_admin/manage_home.html', variables)


def manage_course_syllabus(request, course_year_1, course_year_2, term, course_num, course_group):
    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    syllabus = Syllabus.objects.filter(course_instance=course_instance)

    variables = {'course_instance': course_instance, 'syllabus': syllabus }

    return render(request, 'course_admin/manage_course_syllabus.html', variables)


def manage_course_calendar(request, course_year_1, course_year_2, term, course_num, course_group):

    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    calendar = Calendar.objects.filter(course_instance=course_instance)

    variables = {'course_instance': course_instance, 'calendar': calendar }

    return render(request, 'course_admin/course_calendar.html', variables)


def manage_course_assignments(request, course_year_1, course_year_2, term, course_num, course_group):

    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    assignments = Assignment.objects.filter(course_instance=course_instance)

    variables = {'course_instance': course_instance, 'assignments': assignments }

    return render(request, 'course_admin/manage_course_assignments.html', variables)


def manage_course_grades(request, course_year_1, course_year_2, term, course_num, course_group):

    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    grades = Grade.objects.filter(course_instance=course_instance)

    variables = {'course_instance': course_instance, 'grades': grades }

    return render(request, 'course_admin/manage_course_grades.html', variables)


def manage_course_videolectures(request, course_year_1, course_year_2, term, course_num, course_group):
    # Model is not implemented yet
    return render(request, 'course_admin/manage_course_videolectures.html')


def manage_course_resources(request, course_year_1, course_year_2, term, course_num, course_group):

    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    resources = Resource.objects.filter(course_instance=course_instance)

    variables = {'course_instance': course_instance, 'resources': resources }

    return render(request, 'course_admin/manage_course_resources.html', variables)


def manage_course_forum(request, course_year_1, course_year_2, term, course_num, course_group):

    return render(request, 'course_admin/manage_course_forum.html')


def get_course_instance(course_year_1, course_year_2, term, course_num, course_group):
    SEMESTER = 'SU'
    if ( term == '1' ):
        SEMESTER = 'FA'
    elif ( term == '2' ):
        SEMESTER = 'SP'

    course_instance = CourseInstance.objects.filter(term__year=course_year_1).filter(term__semester=SEMESTER).filter(
        course__course_number=course_num).filter(group=course_group)

    return course_instance