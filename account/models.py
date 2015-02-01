from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    user = models.ForeignKey(User)
    student_id = models.ForeignKey('Student', null=True, blank=True )
    professor_id = models.ForeignKey('Professor', null=True, blank=True )

    def __unicode__(self):
        return self.user.username

class Student(models.Model):
    account_id = models.ForeignKey(Account, null = True, blank = True)
    student_name = models.CharField(max_length=200, null = True, blank = True )
    student_email = models.EmailField( null = True, blank = True )
    student_number = models.PositiveIntegerField( null = True, blank = True )
    degree_level = models.PositiveSmallIntegerField( null = True, blank = True )
    website = models.URLField( null = True, blank = True )

class Professor(models.Model):
    ASSOCIATE_PROFESSOR = 'ASSO'
    ASSISTANT_PROFESSOR = 'ASSI'
    PROFESSOR = 'PROF'

    PROFESSOR_CHOICES = (
        ( ASSISTANT_PROFESSOR, 'Associate Professor' ),
        ( ASSISTANT_PROFESSOR, 'Assistant Professor' ),
        ( PROFESSOR, 'Professor' ),
    )

    account_id = models.ForeignKey(Account, null = True, blank = True )
    # room
    professor_name = models.CharField(max_length=200, null = True, blank = True )
    professor_email = models.EmailField( null = True, blank = True )
    telephone = models.PositiveIntegerField( null = True, blank = True )
    research_interest = models.TextField( null = True, blank = True )
    education_background = models.TextField( null = True, blank = True )
    type = models.CharField( max_length=4, choices=PROFESSOR_CHOICES, null = True, blank = True )
    website = models.URLField( null = True, blank = True )
    # role

    def __unicode__(self):
        return self.account_id.user.first_name + " " + self.account_id.user.last_name
