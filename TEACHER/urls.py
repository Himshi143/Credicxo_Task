from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.CreateTeacherView.as_view()),
    path('all/', views.ListTeacherView.as_view()),
]
