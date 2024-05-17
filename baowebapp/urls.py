from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('', views.main, name='main'),
    path('addMember/', views.addMember, name='addMember'),
    path('updateMember/<str:pk>/', views.updateMember, name='updateMember'),
    path('deleteMember/<str:pk>', views.deleteMember, name='deleteMember'),
]