import json

# from course.models import Course
# from course.models import CourseInstance

with open('./items.json','r') as courses:
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

        print courseID
        break