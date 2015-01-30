from django.shortcuts import render
from django.http import Http404

from course.models import CourseInstance
from course.models import Syllabus
from course.models import Calendar
from course.models import Assignment
from course.models import Grade
from course.models import Resource
from course.models import Topic
from course.models import RoomReservation
from course.models import Post

from course.forms import PostForm


def courses(request):
    return render(request, 'course/courses.html')


def courses_of_term(request, course_year_1, course_year_2, term):
    course_instance_list = CourseInstance.objects.filter(term__year=course_year_1).filter(term__semester=term)

    context = {'course_instance_list': course_instance_list}

    return render(request, 'course/courses.html', context)


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

    context = {'course_instance': course_instance, 'syllabus': syllabus}

    return render(request, 'course/course_syllabus.html', context)


def course_calendar(request, course_year_1, course_year_2, term, course_num, course_group):
    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    calendar = Calendar.objects.filter(course_instance=course_instance)

    context = {'course_instance': course_instance, 'calendar': calendar}

    return render(request, 'course/course_calendar.html', context)


def course_assignments(request, course_year_1, course_year_2, term, course_num, course_group):
    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    assignments = Assignment.objects.filter(course_instance=course_instance)

    context = {'course_instance': course_instance, 'assignments': assignments}

    return render(request, 'course/course_assignments.html', context)


def course_grades(request, course_year_1, course_year_2, term, course_num, course_group):
    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    grades = Grade.objects.filter(course_instance=course_instance)

    context = {'course_instance': course_instance, 'grades': grades}

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
    if ( request.method == 'POST' ):
        print "pooooooost"
        post_form = PostForm(request.POST)
        if ( post_form.is_valid() ):
            print "valiiiiiid"
            post_form.save()
        else:
            print "not valid :("
    else:
        post_form = PostForm()

    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    topics = Topic.objects.filter(course_instance=course_instance)

    context = {'course_instance': course_instance, 'topics': topics, 'form': post_form}

    if ( request.GET.get('topic') != None ):
        topic = Topic.objects.get(id=request.GET.get('topic'))
        posts = Post.objects.filter(topic=topic).filter(parent__isnull=True)

        if ( topic == None ):
            raise Http404("Topic does not exist")

        context['topic'] = topic
        context['posts'] = posts

    return render(request, 'course/course_forum.html', context)


def get_course_instance(course_year_1, course_year_2, term, course_num, course_group):
    course_instance = CourseInstance.objects.filter(term__year=course_year_1).filter(term__semester=term).filter(
        course__course_number=course_num).filter(group=course_group)[:1]

    if ( len(course_instance) == 1 ):
        course_instance = course_instance.get()
    else:
        course_instance = None

    return course_instance