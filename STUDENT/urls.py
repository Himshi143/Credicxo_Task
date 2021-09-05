from django.urls import path
from . import views

urlpatterns = [
    path('add-student/', views.CreateStudentView.as_view()),
    path('list-student/', views.ListStudentView.as_view()),
    path('profile/', views.DetailStudentView.as_view()),
]



# Class based view's default method is as_view()
