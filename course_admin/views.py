from django.shortcuts import render

from course.models import CourseInstance
from course.models import Syllabus
from course.models import Calendar
from course.models import Assignment
from course.models import Grade
from course.models import Resource
from course.models import Topic

from course_admin.forms import CalendarForm

from course.views import get_course_instance

import datetime

# Create your views here.

def manage_course_page(request, course_year_1, course_year_2, term, course_num, course_group):
    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)

    context = {'course_instance': course_instance}

    return render(request, 'course_admin/manage_course_page.html', context)


def manage_course_syllabus(request, course_year_1, course_year_2, term, course_num, course_group):
    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    syllabus = Syllabus.objects.filter(course_instance=course_instance)

    context = {'course_instance': course_instance, 'syllabus': syllabus }

    return render(request, 'course_admin/manage_course_syllabus.html', context)


def manage_course_calendar(request, course_year_1, course_year_2, term, course_num, course_group):

    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)

    if( request.method == 'POST' ):
        form = CalendarForm(request.POST)
        if( form.is_valid() ):
            cal = form.save(commit=False)
            cal.course_instance = course_instance
            cal.save()

            form = CalendarForm()
    else:
        form = CalendarForm()


    calendar_items = Calendar.objects.filter(course_instance=course_instance).order_by('date')

    context = {'course_instance': course_instance, 'calendar_items': calendar_items, 'form': form }

    return render(request, 'course_admin/manage_course_calendar.html', context)


def manage_course_assignments(request, course_year_1, course_year_2, term, course_num, course_group):

    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    assignments = Assignment.objects.filter(course_instance=course_instance)

    context = {'course_instance': course_instance, 'assignments': assignments }

    return render(request, 'course_admin/manage_course_assignments.html', context)


def manage_course_grades(request, course_year_1, course_year_2, term, course_num, course_group):

    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    # grades = Grade.objects.filter(course_instance=course_instance)

    context = {'course_instance': course_instance }

    return render(request, 'course_admin/manage_course_grades.html', context)


def manage_course_videolectures(request, course_year_1, course_year_2, term, course_num, course_group):
    # Model is not implemented yet
    return render(request, 'course_admin/manage_course_videolectures.html')


def manage_course_resources(request, course_year_1, course_year_2, term, course_num, course_group):

    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    # resources = Resource.objects.filter(course_instance=course_instance)

    context = {'course_instance': course_instance }

    return render(request, 'course_admin/manage_course_resources.html', context)


def manage_course_forum(request, course_year_1, course_year_2, term, course_num, course_group):

    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)

    context = {'course_instance': course_instance }


    return render(request, 'course_admin/manage_course_forum.html', context )