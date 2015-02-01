from django.shortcuts import render

from course.models import CourseInstance
from course.models import Syllabus
from course.models import Calendar
from course.models import Assignment
from course.models import Grade
from course.models import GradeItem
from course.models import Resource
from course.models import Topic
from account.models import Student

from course_admin.forms import CalendarForm

from course.views import get_course_instance

from django_ajax.decorators import ajax

import datetime
import json

# Create your views here.

def manage_course_page(request, course_year_1, course_year_2, term, course_num, course_group):
    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)

    context = {'course_instance': course_instance}

    return render(request, 'course_admin/manage_course_page.html', context)


def manage_course_syllabus(request, course_year_1, course_year_2, term, course_num, course_group):
    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    syllabus = Syllabus.objects.filter(course_instance=course_instance)

    context = {'course_instance': course_instance, 'syllabus': syllabus}

    return render(request, 'course_admin/manage_course_syllabus.html', context)


def manage_course_calendar(request, course_year_1, course_year_2, term, course_num, course_group):
    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)

    if ( request.method == 'POST' ):
        form = CalendarForm(request.POST)
        if ( form.is_valid() ):
            cal = form.save(commit=False)
            cal.course_instance = course_instance
            cal.save()

            form = CalendarForm()
    else:
        form = CalendarForm()

    calendar_items = Calendar.objects.filter(course_instance=course_instance).order_by('date')

    context = {'course_instance': course_instance, 'calendar_items': calendar_items, 'form': form}

    return render(request, 'course_admin/manage_course_calendar.html', context)


def manage_course_assignments(request, course_year_1, course_year_2, term, course_num, course_group):
    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    assignments = Assignment.objects.filter(course_instance=course_instance)

    context = {'course_instance': course_instance, 'assignments': assignments}

    return render(request, 'course_admin/manage_course_assignments.html', context)


def manage_course_grades(request, course_year_1, course_year_2, term, course_num, course_group):
    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    grade_items_HW = GradeItem.objects.filter(course_instance=course_instance).filter(grade_type='AS')
    grade_items_PR = GradeItem.objects.filter(course_instance=course_instance).filter(grade_type='PR')
    grade_items_EX = GradeItem.objects.filter(course_instance=course_instance).filter(grade_type='EX')
    grade_items_FI = GradeItem.objects.filter(course_instance=course_instance).filter(grade_type='FI')
    grade_items_OT = GradeItem.objects.filter(course_instance=course_instance).filter(grade_type='OT')

    context = {'course_instance': course_instance, 'grade_items_HW': grade_items_HW, 'grade_items_PR': grade_items_PR,
               'grade_items_EX': grade_items_EX, 'grade_items_FI': grade_items_FI, 'grade_items_OT': grade_items_OT}

    return render(request, 'course_admin/manage_course_grades.html', context)


def manage_course_videolectures(request, course_year_1, course_year_2, term, course_num, course_group):
    # Model is not implemented yet
    return render(request, 'course_admin/manage_course_videolectures.html')


def manage_course_resources(request, course_year_1, course_year_2, term, course_num, course_group):
    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    # resources = Resource.objects.filter(course_instance=course_instance)

    context = {'course_instance': course_instance}

    return render(request, 'course_admin/manage_course_resources.html', context)


def manage_course_forum(request, course_year_1, course_year_2, term, course_num, course_group):
    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)

    context = {'course_instance': course_instance}

    return render(request, 'course_admin/manage_course_forum.html', context)


@ajax
def add_course_grades(request, course_year_1, course_year_2, term, course_num, course_group):
    # make new Grade Item

    # gi = GradeItem(  )

    dic = request.POST.dict()
    key, value = dic.popitem()

    j = json.loads(key)

    # TODO: Very unefficient
    for item in j:
        if ( item[0] == 'grade_item_title' ):
            grade_item_title = item[1]
        if ( item[0] == 'grade_item_type' ):
            grade_item_type = item[1]

    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    grade_item = GradeItem(course_instance=course_instance, title=grade_item_title, grade_type=grade_item_type,
                           max_grade=20)
    grade_item.save()

    for item in j:
        student_number = item[0]
        grade = item[1]

        if (
                        student_number == None or student_number == "ID" or student_number == "grade_item_type" or student_number == "grade_item_title" ):
            continue

        student_number = int(student_number)

        student = Student.objects.filter(student_number=student_number)
        if ( len(student) == 1 ):
            student = student.get()
            grade_object = Grade(grade_item=grade_item, student=student, grade=grade)
            grade_object.save()
        else:
            grade_object = Grade(grade_item=grade_item, student_number=student_number, grade=grade)
            grade_object.save()

    return "shayan"
