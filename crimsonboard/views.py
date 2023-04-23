from django.utils import timezone
from django.shortcuts import render
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt            #to submit form in django
from django.http import JsonResponse,HttpResponse
from .serializers import InstructorSerializer, CategorySerializer, CourseSerializer, ModuleSerializer, AssignmentResponseSerializer,\
    AssignmentSerializer, StudentSerializer, StudentCourseEnrollmentSerializer, InstructorDashboardSerializer
from . import models
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions
from datetime import datetime as dt
import json

#To get a list of instructors
class InstructorList(generics.ListCreateAPIView):
    queryset = models.Instructor.objects.all()
    serializer_class = InstructorSerializer
    #permission_classes = [permissions.IsAuthenticated]

#To get a list of students
class StudentList(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
    #permission_classes = [permissions.IsAuthenticated]

#To view,update or delete a particular instructor
class InstructorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Instructor.objects.all()
    serializer_class = InstructorSerializer
    #permission_classes = [permissions.IsAuthenticated]

class InstructorDashboard(generics.RetrieveAPIView):
    queryset = models.Instructor.objects.all()
    serializer_class = InstructorDashboardSerializer

#To view,update or delete a particular studenr
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
    #permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
def instructor_login(request):
    email = request.POST['email']
    password = request.POST['password']
    try:
        instructorData = models.Instructor.objects.get(email=email, password=password)
        instructorData.login_time = timezone.now()
        instructorData.save(update_fields=['login_time'])
    except models.Instructor.DoesNotExist:
        instructorData = None
    if instructorData:
        return JsonResponse({'bool': True, 'instructor_id': instructorData.id}) 
    else:
        return JsonResponse({'bool': False})

@csrf_exempt
def student_login(request):
    email = request.POST['email']
    password = request.POST['password']
    try:
        studentData = models.Student.objects.get(email=email, password=password)
        studentData.login_time = timezone.now()
        studentData.save(update_fields=['login_time'])
    except models.Student.DoesNotExist:
        studentData = None
    if studentData:
        return JsonResponse({'bool': True, 'student_id': studentData.id}) 
    else:
        return JsonResponse({'bool': False})

class CategoryList(generics.ListCreateAPIView):
    queryset = models.CourseCategory.objects.all()
    serializer_class = CategorySerializer

#This returns all the courses present
class CourseList(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'res' in self.request.GET:
            limit = int(self.request.GET['res'])
            qs = models.Course.objects.all().order_by('-id')[:limit]
        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring']
            qs = models.Course.objects.filter(Q(technologies__icontains=search) | Q(title__icontains=search) | Q(course_modules__icontains=search) | Q(course_assignments__icontains=search))
        return qs

class CourseDetailView(generics.RetrieveAPIView):
    queryset =  models.Course.objects.all()
    serializer_class = CourseSerializer

#This class is to generate courses for corresponding teacher
class InstructorCourseList(generics.ListAPIView):
    serializer_class = CourseSerializer

    #override queryset
       # To retrieve the instructor ID from the URL, fetch the corresponding Instructor object, and return all the 
        #courses associated with that instructor. 
    def get_queryset(self):                                  
        instructor_id = self.kwargs['instructor_id']
        instructor = models.Instructor.objects.get(pk = instructor_id)
        return models.Course.objects.filter(instructor=instructor)
    
class InstructorCourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer
    
class ModuleList(generics.ListCreateAPIView):
    queryset = models.Module.objects.all()
    serializer_class = ModuleSerializer

class AssignmentList(generics.ListCreateAPIView):
    queryset = models.Assignments.objects.all()
    serializer_class = AssignmentSerializer

class AssignmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Assignments.objects.all()
    serializer_class = AssignmentSerializer

class AssignmentResponseList(generics.ListCreateAPIView):
    queryset = models.AssignmentResponse.objects.all()
    print("queryset : ", queryset)
    serializer_class = AssignmentResponseSerializer

class AssignmentResponseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AssignmentResponse.objects.all()
    print("Retrieve qset 2: ", queryset)
    serializer_class = AssignmentResponseSerializer

#This class is to generate all modules for a specific course
class CourseModuleList(generics.ListAPIView):
    serializer_class = ModuleSerializer

    #override queryset
       # To retrieve the course ID from the URL, fetch the corresponding course object, and return all the 
        #chapter associated with that course. 
    def get_queryset(self):                                  
        course_id = self.kwargs['course_id']
        course = models.Course.objects.get(pk = course_id)
        return models.Module.objects.filter(course=course)


class ModuleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Module.objects.all()
    serializer_class = ModuleSerializer

class StudentCourseEnrollmentList(generics.ListCreateAPIView):
    queryset = models.StudentCourseEnrollment.objects.all()
    serializer_class = StudentCourseEnrollmentSerializer

def fetch_enroll_status(request, student_id, course_id):
    # print('This is called')
    student=models.Student.objects.get(id=student_id)
    course=models.Course.objects.get(id=course_id)
    enrollStatus=models.StudentCourseEnrollment.objects.filter(course=course, student=student).first()
    
    if enrollStatus:
        # print('This is True')
        return JsonResponse({'bool': True})
        
    else:
        # print('This is False')
        return JsonResponse({'bool': False})

class EnrolledStudentList(generics.ListAPIView):
    # print('This is called')
    queryset = models.StudentCourseEnrollment.objects.all()
    serializer_class = StudentCourseEnrollmentSerializer
    
    def get_queryset(self):
        # print('queryset called')
        # print(self.kwargs)
        if 'course_id' in self.kwargs:
            return_value = models.StudentCourseEnrollment.objects.distinct('id')
            return return_value
        if 'instructor_id' in self.kwargs:
            instructor_id = self.kwargs['instructor_id']
            instructor = models.Instructor.objects.get(pk=instructor_id)
            print(instructor)
            return models.StudentCourseEnrollment.objects.filter(course__instructor=instructor)
        if 'student_id' in self.kwargs:
            student_id = self.kwargs['student_id']
            student = models.Student.objects.get(pk=student_id)
            return models.StudentCourseEnrollment.objects.filter(student=student)
            

@csrf_exempt
def instructor_change_password(request, instructor_id):
    print('This')
    print(request)
    password = request.POST['password']
    print('THis is pwd:', password)
    try:
        instructorData = models.Instructor.objects.get(id=instructor_id)
    except models.Instructor.DoesNotExist:
        instructorData = None
    if instructorData:
        models.Instructor.objects.filter(id=instructor_id).update(password=password)
        return JsonResponse({'bool': True}) 
    else:
        return JsonResponse({'bool': False})

def view_instructor_course_assignments(request, instructor_id, course_id):
    instructor=models.Instructor.objects.get(id=instructor_id)
    course=models.Course.objects.get(id=course_id)
    assignment=models.Assignments.objects.filter(course=course, instructor=instructor)
    
    # print(assignment)
    response = []
    for a in assignment:
        obj = {}
        obj['id'] = a.id
        obj["title"] = a.title
        obj["creation_time"] = a.creation_time.strftime("%m/%d/%Y, %H:%M:%S")
        obj["deadline"] = a.deadline.strftime("%m/%d/%Y, %H:%M:%S")
        response.append(obj)
    
    return JsonResponse({'response': response}) 

def testjson(self):
    print("In here")

    msg = "Hi Hello Team, welcome to the JsonAPI"
    return JsonResponse({'Status':'Success', 'msg' : msg})

def homeview(request):
    return render(request, './crimsonboard/index.html', {})

