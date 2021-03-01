from core import views 
from django.urls import path


urlpatterns = [
    path('students/', views.StudentsListView.as_view(), name='students-list'),
    path('campus/', views.CampusListView.as_view(), name='campus-list'),
    path('numberofstudents/', views.NumberOfStudentsListView.as_view(), name='number-students-list'),
    path('students/create', views.CreateStudent.as_view(), name='create-student'),
    path('searchstudent/', views.SearchStudent.as_view(), name='search-student'),
    path('students/<str:ra>/<str:campus>/', views.StudentsDetail.as_view(), name='students-detail')

]

