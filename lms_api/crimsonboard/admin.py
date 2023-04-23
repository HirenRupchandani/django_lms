from django.contrib import admin
from . import models

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('login_time', 'logout_time', )

# admin.site.register(Rating,RatingAdmin)

admin.site.register(models.Instructor, UserAdmin)
admin.site.register(models.Course)
admin.site.register(models.Module)
admin.site.register(models.CourseCategory)
admin.site.register(models.Student, UserAdmin)
admin.site.register(models.StudentCourseEnrollment)
admin.site.register(models.Assignments)
admin.site.register(models.AssignmentResponse)