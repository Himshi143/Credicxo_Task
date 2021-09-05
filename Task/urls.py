from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/auth/', include('AUTH.urls')),
    path('api/teacher/', include('TEACHER.urls')),
    path('api/student/', include('STUDENT.urls')),
]
