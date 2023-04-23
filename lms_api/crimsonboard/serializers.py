# import datetime module
from datetime import datetime
from rest_framework import serializers
from . import models

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Instructor
        fields = ['id','full_name', 'email', 'bio', 'qualification', 'mobile_number', 'profile_img', 'password']

class InstructorDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Instructor
        fields = ['total_teacher_courses']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ['id','title','description']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id','category','instructor','title','description', 'course_image', 'technologies','course_modules','total_enrolled_students', 'course_assignments']
        depth = 1 #to retrieve the next level relationship
    
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Module
        fields = ['id','course','title','description','video','remarks']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id','full_name', 'email','username','password','interested_categories']

class StudentCourseEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentCourseEnrollment
        fields = ['id', 'course', 'student', 'enrolled_time']
        depth=1 
    def __init__(self, *args, **kwargs):
        super(StudentCourseEnrollmentSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method=='POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 2

class AssignmentSerializer(serializers.ModelSerializer):
    # deadline = 
    # deadline = datetime.strptime(my_date, "%d-%b-%Y-%H:%M:%S")
    class Meta:
        model = models.Assignments
        fields = ['id', 'course', 'instructor', 'title', 'description', 'deadline', 'assignment_file', 'assignmentSubmissions']
    def __init__(self, *args, **kwargs):
        super(AssignmentSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method=='POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 2

class AssignmentResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AssignmentResponse
        fields = ['id', 'assignment', 'course', 'student', 'reponse_text', 'submission_file', 'submission_time', 'grade']
        # depth=1
        
    def __init__(self, *args, **kwargs):
        super(AssignmentResponseSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method=='POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1