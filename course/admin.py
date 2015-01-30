from django.contrib import admin
from course import models

# Register your models here.

admin.site.register(models.Course)
admin.site.register(models.Announcement)
admin.site.register(models.Assignment)
admin.site.register(models.Calendar)
admin.site.register(models.Choice)
admin.site.register(models.Choosed_Choice)
admin.site.register(models.CourseInstance)
admin.site.register(models.Grade)
admin.site.register(models.GradeItem)
admin.site.register(models.Poll)
admin.site.register(models.Post)
admin.site.register(models.Resource)
admin.site.register(models.Room)
admin.site.register(models.RoomReservation)
admin.site.register(models.Syllabus)
admin.site.register(models.Term)
admin.site.register(models.Topic)
admin.site.register(models.TextBook)
admin.site.register(models.UploadedAssignment)