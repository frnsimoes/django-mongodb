from core.views import StudentsListView
from django.urls import path

urlpatterns = [
    path('', StudentsListView.as_view({'get': 'list'}), name= 'students-list')
]
