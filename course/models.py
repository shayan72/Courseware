from django.db import models

# Abstract Course
class Course(models.Model):
    name = models.CharField(max_length=200)
    course_number = models.PositiveIntegerField()
    credit = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.name

class Term(models.Model):

    FALL =  'FA'
    SPRING = 'SP'
    SUMMER = 'SU'

    SEMESTER_CHOICES = (
        ( FALL, 'Fall' ),
        ( SPRING, 'Spring' ),
        ( SUMMER, 'Summer' ),
    )

    year = models.IntegerField() #TODO year field
    semester = models.CharField( max_length=2, choices=SEMESTER_CHOICES )

    def __unicode__(self):
        d = dict(self.SEMESTER_CHOICES)
        return self.year.__str__() + "-" + (self.year+1).__str__() + " " + d[self.semester]

# Each Real Course
class CourseInstance(models.Model):
    course = models.ForeignKey(Course)
    term = models.ForeignKey(Term)
    group = models.SmallIntegerField()
    professors = models.ManyToManyField('account.Professor')
    teacher_assistants = models.ManyToManyField('account.Student', null = True, blank = True, related_name='course_teacher_assistants' )
    description = models.TextField( null = True, blank = True )
    picture = models.ImageField( null = True, blank = True )
    students = models.ManyToManyField('account.Student', null = True, blank = True, related_name='course_students' )

    def __unicode__(self):
        return self.course.course_number.__str__() + " " + self.course.name + " " + self.term.__str__()

class Room(models.Model):
    number = models.PositiveSmallIntegerField()

class RoomReservation(models.Model):

    #TODO room reservation not for main class or TA class

    SATURDAY = 'SA'
    SUNDAY = 'SU'
    MONDAY = 'MO'
    TUESDAY = 'TU'
    WEDNESDAY = 'WE'
    THURSDAY = 'TH'
    FRIDAY = 'FR'

    DAY_CHOICES = (
        ( SATURDAY, 'Saturday' ),
        ( SUNDAY, 'Sunday' ),
        ( MONDAY, 'Monday' ),
        ( TUESDAY, 'Tuesday' ),
        ( WEDNESDAY, 'Wednesday' ),
        ( THURSDAY, 'Thursday' ),
        ( FRIDAY, 'Friday' ),
    )

    course_instance = models.ForeignKey(CourseInstance)
    room_id = models.ForeignKey(Room)
    day = models.CharField( max_length=2, choices=DAY_CHOICES )
    start_time = models.TimeField()
    finish_time = models.TimeField()
    is_ta = models.BooleanField(default=False)

class Announcement(models.Model):
    created_by = models.ForeignKey('account.Account')
    course_instance = models.ForeignKey(CourseInstance)
    body = models.TextField()
    created_at = models.DateTimeField()

class Calendar(models.Model):
    course_instance = models.ForeignKey(CourseInstance)
    subject = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField()

class TextBook(models.Model):
    name = models.CharField(max_length=1000)
    link = models.URLField()

class Syllabus(models.Model):
    course_instance = models.ForeignKey(CourseInstance)
    description = models.TextField()
    text_books = models.ManyToManyField(TextBook, null=True, blank=True)
    grading_policy = models.TextField( null=True, blank=True )

class Assignment(models.Model):
    course_instance = models.ForeignKey(CourseInstance)
    created_by = models.ForeignKey('account.Account')
    description = models.TextField()
    link = models.URLField()
    deadline = models.DateTimeField()
    created_at = models.DateTimeField()

class UploadedAssignment(models.Model):
    assignment = models.ForeignKey(Assignment)
    student = models.ForeignKey('account.Student')
    link = models.URLField()
    created_at = models.DateTimeField()


class GradeItem(models.Model):
    course_instance = models.ForeignKey(CourseInstance)
    title = models.CharField( max_length=200 )
    assignment = models.ForeignKey(Assignment, null=True, blank=True )
    # quiz
    max_grade = models.PositiveIntegerField()
    coefficient = models.PositiveIntegerField()

class Grade(models.Model):
    student = models.ForeignKey('account.Student')
    grade = models.PositiveIntegerField()

class Resource(models.Model):
    name = models.CharField(max_length=1000)
    link = models.URLField()
    # type

class Topic(models.Model):
    course_instance = models.ForeignKey(CourseInstance)
    created_by = models.ForeignKey('account.Account')
    title = models.CharField( max_length=200 )
    body = models.TextField()
    view_num = models.IntegerField( default=0 )
    locked = models.BooleanField( default=False )
    anonymous = models.BooleanField( default=False )
    created_at = models.DateTimeField()

class Post(models.Model):
    topic = models.ForeignKey(Topic)
    created_by = models.ForeignKey('account.Account')
    body = models.TextField()
    anonymous = models.BooleanField( default=False )
    created_at = models.DateTimeField()

class Poll(models.Model):
    topic = models.OneToOneField(Topic)

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Choosed_Choice(models.Model):
    poll = models.ForeignKey(Poll)
    voted_by = models.ForeignKey('account.Account')
    choice = models.ForeignKey(Choice)