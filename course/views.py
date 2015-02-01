from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required

from course.models import CourseInstance
from course.models import Syllabus
from course.models import Calendar
from course.models import Assignment
from course.models import Grade
from course.models import GradeItem
from course.models import Resource
from course.models import Topic
from course.models import RoomReservation
from course.models import Post
from course.models import Term
from account.models import Account

from course.forms import PostForm, TopicForm

from django.middleware.csrf import get_token
from django.template import RequestContext

from ajaxuploader.views import AjaxFileUploader

import datetime

def courses(request, course_year_1 = 93, course_year_2 = 94, term = 'FA' ):
    course_instance_list = CourseInstance.objects.filter(term__year=course_year_1).filter(term__semester=term)
    terms = Term.objects.all()
    current_term = Term.objects.filter(year=course_year_1).filter(semester=term).get()

    context = {'course_instance_list': course_instance_list, 'terms': terms, 'current_term': current_term }

    return render(request, 'course/courses.html', context )


def course_page(request, course_year_1, course_year_2, term, course_num, course_group):
    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)

    if ( course_instance == None ):
        raise Http404("Course does not exist")

    room_reservations = RoomReservation.objects.filter(course_instance=course_instance.id)

    context = {'course_instance': course_instance, 'room_reservations': room_reservations}

    return render(request, 'course/course_page.html', context)


def course_syllabus(request, course_year_1, course_year_2, term, course_num, course_group):
    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    syllabus = Syllabus.objects.filter(course_instance=course_instance)

    if( len(syllabus) == 1 ):
        syllabus = syllabus.get()
    else:
        syllabus = None

    context = {'course_instance': course_instance, 'syllabus': syllabus}

    return render(request, 'course/course_syllabus.html', context)


def course_calendar(request, course_year_1, course_year_2, term, course_num, course_group):
    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    calendar_items = Calendar.objects.filter(course_instance=course_instance)

    context = {'course_instance': course_instance, 'calendar_items': calendar_items}

    return render(request, 'course/course_calendar.html', context)


def course_assignments(request, course_year_1, course_year_2, term, course_num, course_group):

    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    assignments = Assignment.objects.filter(course_instance=course_instance).order_by('-id')

    csrf_token = get_token(request)

    context = {'course_instance': course_instance, 'assignments': assignments, 'csrf_token': csrf_token }

    return render(request, 'course/course_assignments.html', context)


import_uploader = AjaxFileUploader()


def course_grades(request, course_year_1, course_year_2, term, course_num, course_group):

    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    grade_items_HW = GradeItem.objects.filter(course_instance=course_instance).filter(grade_type='AS')
    grade_items_PR = GradeItem.objects.filter(course_instance=course_instance).filter(grade_type='PR')
    grade_items_EX = GradeItem.objects.filter(course_instance=course_instance).filter(grade_type='EX')
    grade_items_FI = GradeItem.objects.filter(course_instance=course_instance).filter(grade_type='FI')
    grade_items_OT = GradeItem.objects.filter(course_instance=course_instance).filter(grade_type='OT')

    context = {'course_instance': course_instance, 'grade_items_HW': grade_items_HW, 'grade_items_PR': grade_items_PR,
               'grade_items_EX': grade_items_EX, 'grade_items_FI': grade_items_FI, 'grade_items_OT': grade_items_OT}

    return render(request, 'course/course_grades.html', context)


def course_videolectures(request, course_year_1, course_year_2, term, course_num, course_group):
    # Model is not implemented yet
    return render(request, 'course/course_videolectures.html')


def course_resources(request, course_year_1, course_year_2, term, course_num, course_group):
    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    resources = Resource.objects.filter(course_instance=course_instance)

    context = {'course_instance': course_instance, 'resources': resources}

    return render(request, 'course/course_resources.html', context)


def course_forum(request, course_year_1, course_year_2, term, course_num, course_group):

    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    topics = Topic.objects.filter(course_instance=course_instance)
    topic_form = TopicForm()
    post_form = PostForm()

    context = {'course_instance': course_instance, 'topics': topics, 'form': post_form, 'topic_form': topic_form }

    if ( request.GET.get('topic') is not None ):
        topic = Topic.objects.get(id=request.GET.get('topic'))
        posts = Post.objects.filter(topic=topic).filter(parent__isnull=True)

        if ( topic == None ):
            raise Http404("Topic does not exist")

        context['topic'] = topic
        context['posts'] = posts

    return render(request, 'course/course_forum.html', context)

@login_required
def course_forum_add_post(request, course_year_1, course_year_2, term, course_num, course_group):

    if ( request.method == 'POST' ):
        post_form = PostForm(request.POST)
        if ( post_form.is_valid() ):
            body = post_form.cleaned_data['body']
            anonymous = post_form.cleaned_data['anonymous']
            created_by = Account.objects.get(user=request.user)
            topic = Topic.objects.get(id=request.POST.get('topic')) #TODO: check if we are in topic
            parent = None
            if( request.POST.__contains__('parent_post') ):
                parent = Post.objects.get(id=request.POST.get('parent_post'))
            post = Post( topic=topic, created_by=created_by, body=body, anonymous=anonymous, parent=parent )
            post.save()

        else:
            print "not valid :("

    response = redirect('course_forum', course_year_1, course_year_2, term, course_num, course_group)
    response['Location'] += '?topic=' + request.POST.get('topic')
    return response

@login_required
def course_forum_add_topic(request, course_year_1, course_year_2, term, course_num, course_group):

    if ( request.method == 'POST' ):
        topic_form = TopicForm(request.POST)
        if ( topic_form.is_valid() ):
            title = topic_form.cleaned_data['title']
            body = topic_form.cleaned_data['body']
            anonymous = topic_form.cleaned_data['anonymous']

            course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
            created_by = Account.objects.get(user=request.user)
            topic = Topic(course_instance=course_instance, created_by=created_by, title=title, anonymous=anonymous )
            topic.save()

            post = Post( topic=topic, created_by=created_by, body=body, anonymous=anonymous )
            post.save()

        else:
            print "not valid :("

    response = redirect('course_forum', course_year_1, course_year_2, term, course_num, course_group)
    response['Location'] += '?topic=' + str(topic.id)
    return response


def get_course_instance(course_year_1, course_year_2, term, course_num, course_group):
    course_instance = CourseInstance.objects.filter(term__year=course_year_1).filter(term__semester=term).filter(
        course__course_number=course_num).filter(group=course_group)[:1]

    if ( len(course_instance) == 1 ):
        course_instance = course_instance.get()
    else:
        course_instance = None

    return course_instance