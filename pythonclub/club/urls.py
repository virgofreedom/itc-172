from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name='index'),
    path('resourcelist/', views.resourceslist, name='resourcelist'),
    path('meetinglist/', views.meetinglist, name='meetinglist'),
    path('meetingdetail/<int:id>', views.meetingdetail, name='meetingdetail'),
]