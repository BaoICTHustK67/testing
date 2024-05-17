from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.StudentListCreate.as_view(), name="student-view-create"),
    path(
        'students/<str:pk>/',
        views.StudentRetrieveUpdateDestroy.as_view(),
        name="update"
    ),

]