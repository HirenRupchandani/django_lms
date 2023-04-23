from django.urls import path
from . import views

urlpatterns = [
    path('instructor/', views.InstructorList.as_view()),
    path('instructor/<int:pk>/', views.InstructorDetail.as_view()),
    path('instructor-login', views.instructor_login),

    path('category/', views.CategoryList.as_view()),

    path('course/', views.CourseList.as_view()),

    path('course/<int:pk>/', views.CourseDetailView.as_view()),

    path('module/', views.ModuleList.as_view()),

    #all modules for a specified course
     path('course-modules/<int:course_id>', views.CourseModuleList.as_view()),

    #For a specified instructor
    path('instructor-courses/<int:instructor_id>', views.InstructorCourseList.as_view()),

    #Specific course as taught by instructor
    path('instructor-course-detail/<int:pk>', views.InstructorCourseDetail.as_view()), 
    # Dashboard
    path('instructor/dashboard/<int:pk>', views.InstructorDashboard.as_view()), 

    #For a specified module
    path('module/<int:pk>', views.ModuleDetailView.as_view()),

    path('search-courses/<str:searchstring>', views.CourseList.as_view()),

    path('student/',views.StudentList.as_view()),

    path('student-login',views.student_login),
    path('instructor/change-password/<int:instructor_id>',views.instructor_change_password),
    
    path('student-enroll-course/',views.StudentCourseEnrollmentList.as_view()),
    path('fetch-enroll-status/<int:student_id>/<int:course_id>/',views.fetch_enroll_status),
    path('fetch-all-enrolled-students/<int:instructor_id>',views.EnrolledStudentList.as_view()),
    path('fetch-enrolled-students/<int:course_id>',views.EnrolledStudentList.as_view()),
    path('fetch-all-enrolled-students/<int:instructor_id>',views.EnrolledStudentList.as_view()),
    
    path('fetch-enrolled-courses/<int:student_id>',views.EnrolledStudentList.as_view()),
    
    # Assignments
    path('assignment/', views.AssignmentList.as_view()),
    path('assignment/<int:pk>', views.AssignmentDetail.as_view()),
    
    # path('student-course-assignment/<int:course_id>', views.view_instructor_course_assignments),
    path('view-course-assignment/<int:instructor_id>/<int:course_id>', views.view_instructor_course_assignments),
    path('assignmentResponse/', views.AssignmentResponseList.as_view()),
    path('assignmentResponse/<int:pk>/', views.AssignmentResponseDetail.as_view()),
]