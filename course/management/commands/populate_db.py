from django.core.management.base import BaseCommand

from course.models import Course
from course.models import CourseInstance

import json

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_tags(self):

        with open('/Users/shayansalehian/Documents/WebWorkspace/Courseware/crawler/out/items.json','r') as courses:
            for line in courses:
                item=json.loads(line[:-2])
                try:
                    courseID=item['courseID']
                except:
                    pass
                try:
                    courseName=item['courseName']
                except:
                    pass
                try:
                    link=item['link']
                except:
                    pass
                try:
                    teacher=item['teacher']
                except:
                    pass
                print link
                # course_instance = CourseInstance(  )
                break

    def handle(self, *args, **options):
        self._create_tags()