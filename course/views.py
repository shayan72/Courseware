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


def courses(request):
    return render(request, 'course/courses.html')

def courses_of_term(request, course_year_1, course_year_2, term):
    course_instance_list = CourseInstance.objects.filter(term__year=course_year_1).filter(term__semester=term)

    variables = {'course_instance_list': course_instance_list}

    return render(request, 'course/courses.html', variables)


def course_page(request, course_year_1, course_year_2, term, course_num, course_group):
    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)

    if ( course_instance == None ):
        raise Http404("Course does not exist")

    room_reservations = RoomReservation.objects.filter(course_instance=course_instance.id)

    variables = {'course_instance': course_instance, 'room_reservations': room_reservations}

    return render(request, 'course/course_page.html', variables)


def course_syllabus(request, course_year_1, course_year_2, term, course_num, course_group):
    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    syllabus = Syllabus.objects.filter(course_instance=course_instance)

    variables = {'course_instance': course_instance, 'syllabus': syllabus}

    return render(request, 'course/course_syllabus.html', variables)


def course_calendar(request, course_year_1, course_year_2, term, course_num, course_group):
    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    calendar = Calendar.objects.filter(course_instance=course_instance)

    variables = {'course_instance': course_instance, 'calendar': calendar}

    return render(request, 'course/course_calendar.html', variables)


def course_assignments(request, course_year_1, course_year_2, term, course_num, course_group):
    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    assignments = Assignment.objects.filter(course_instance=course_instance)

    variables = {'course_instance': course_instance, 'assignments': assignments}

    return render(request, 'course/course_assignments.html', variables)


def course_grades(request, course_year_1, course_year_2, term, course_num, course_group):
    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    grades = Grade.objects.filter(course_instance=course_instance)

    variables = {'course_instance': course_instance, 'grades': grades}

    return render(request, 'course/course_grades.html', variables)


def course_videolectures(request, course_year_1, course_year_2, term, course_num, course_group):
    # Model is not implemented yet
    return render(request, 'course/course_videolectures.html')


def course_resources(request, course_year_1, course_year_2, term, course_num, course_group):
    course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)
    resources = Resource.objects.filter(course_instance=course_instance)

    variables = {'course_instance': course_instance, 'resources': resources}

    return render(request, 'course/course_resources.html', variables)


def course_forum(request, course_year_1, course_year_2, term, course_num, course_group):

    if ( request.method == 'POST' ):
        pass
    elif ( request.method == 'GET' ):

        course_instance = get_course_instance(course_year_1, course_year_2, term, course_num, course_group)

        if ( request.GET.get('topic') == None ):
            topics = Topic.objects.filter(course_instance=course_instance)

            variables = {'course_instance': course_instance, 'topics': topics}
        else:
            topic = Topic.objects.get(id=request.GET.get('topic'))
            posts = Post.objects.filter(topic=topic).filter(parent__isnull=True)

            if( topic == None ):
                raise Http404("Topic does not exist")

            variables = {'course_instance': course_instance, 'topic': topic, 'posts':posts }

    return render(request, 'course/course_forum.html', variables)


def get_course_instance(course_year_1, course_year_2, term, course_num, course_group):
    course_instance = CourseInstance.objects.filter(term__year=course_year_1).filter(term__semester=term).filter(
        course__course_number=course_num).filter(group=course_group)[:1]

    if ( len(course_instance) == 1 ):
        course_instance = course_instance.get()
    else:
        course_instance = None

    return course_instance