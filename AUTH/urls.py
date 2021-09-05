from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.CreateUserView.as_view()),
    path('login/', views.LoginUserView.as_view()),
    path('reset-password/', views.PasswordResetBeginView.as_view()),
]
