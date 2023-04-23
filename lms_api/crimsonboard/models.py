from django.db import models

# Create your models here.

#Instructor Model
class Instructor(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    bio = models.TextField(null=True, default='Bio')
    qualification = models.CharField(max_length=200)
    mobile_number= models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    profile_img = models.ImageField(upload_to='instructor_profile_imgs/', null=True)
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "1. Instructors"
        
    def total_teacher_courses(self):
        total_courses = Course.objects.filter(instructor=self).count()
        return total_courses
    
    # def total_teacher_modules(self):
    #     total_modules = Module.objects.filter(id=self).count()
    #     return total_modules
        
    # def total_teacher_students(self):
    #     total_students = StudentCourseEnrollment.objects.filter(id=self).count()
    #     return total_students

#Course Category Model
class CourseCategory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "2. Course Categories"

    def __str__(self) -> str:
        return self.title;                  #returning just the title from course category

#Course model
class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    course_image = models.ImageField(upload_to= 'course_imgs/', null=True)
    technologies = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "3. Courses"
        
    def __str__(self):
        return self.title
    
    def total_enrolled_students(self):
        total_count = StudentCourseEnrollment.objects.filter(course=self).count()
        return total_count

#Student model
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100, null=True, default='student_dummy')
    mobile_number = models.IntegerField(null=True, default=1234567890)
    address = models.TextField(null=True, default='Bloomington')
    interested_categories = models.TextField()
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name_plural = "4. Students"
    
#Module model
class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_modules")
    title = models.CharField(max_length=100)
    description = models.TextField()
    video = models.FileField(upload_to= 'module_videos/', null=True)
    remarks = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "5. Modules" 

class StudentCourseEnrollment(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrolled_courses")
    student=models.ForeignKey(Student, on_delete=models.CASCADE, related_name="enrolled_students")
    enrolled_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "6. Enrolled Courses"
        
    def __str__(self):
        return f"{self.course}-{self.student}"

class Assignments(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_assignments")
    instructor=models.ForeignKey(Instructor, on_delete=models.CASCADE)
    title=models.CharField(max_length=200, null=True)
    description=models.TextField(null=True)
    creation_time=models.DateTimeField(auto_now_add=True)
    deadline=models.DateTimeField(null=True, blank=True)
    assignment_file=models.FileField(upload_to ='assignments/', null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "7. Assignments" 

class AssignmentResponse(models.Model):
    assignment=models.ForeignKey(Assignments, on_delete=models.CASCADE, related_name='assignmentSubmissions')
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    reponse_text=models.TextField(null=True, default='Submission Done', blank=True)
    submission_file=models.FileField(upload_to ='responses/', null=True)
    submission_time=models.DateTimeField(auto_now_add=True)
    grade=models.FloatField(default=0)
    
    class Meta:
        verbose_name_plural = "8. Assignment Responses"