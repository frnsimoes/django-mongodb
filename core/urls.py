from django.urls.conf import include
from core.views import NumberOfStudentsListView, StudentsListView, CampusListView
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'students', StudentsListView, basename='students')
router.register(r'campus', CampusListView, basename='Campus')
router.register(r'numberofstudents', NumberOfStudentsListView, basename='number-of-students')
# router.register(r'numberofstudents', NumberOfStudentsListView, basename='NumberOfStudents')

urlpatterns = [
    # path('', StudentsListView.as_view({'get': 'list'}), name= 'students-list')
    path('', include(router.urls))
]
