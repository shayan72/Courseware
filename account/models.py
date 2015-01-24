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
    account_id = models.ForeignKey(Account)
    student_number = models.PositiveIntegerField()
    degree_level = models.PositiveSmallIntegerField()
    website = models.URLField()

class Professor(models.Model):
    ASSOCIATE_PROFESSOR = 'ASSO'
    ASSISTANT_PROFESSOR = 'ASSI'
    PROFESSOR = 'PROF'

    PROFESSOR_CHOICES = (
        ( ASSISTANT_PROFESSOR, 'Associate Professor' ),
        ( ASSISTANT_PROFESSOR, 'Assistant Professor' ),
        ( PROFESSOR, 'Professor' ),
    )

    account_id = models.ForeignKey(Account)
    # room
    telephone = models.PositiveIntegerField()
    research_interest = models.TextField()
    education_background = models.TextField()
    type = models.CharField( max_length=4, choices=PROFESSOR_CHOICES )
    website = models.URLField()
    # role

