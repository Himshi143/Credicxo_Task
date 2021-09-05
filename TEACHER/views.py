from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import BasePermission
from .models import Teacher
from .serializers import CreateTeacherSerializer, ListTeacherSerializer


# Custom Permission, class in Django
class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        return False


class CreateTeacherView(CreateAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = CreateTeacherSerializer
    queryset = Teacher.objects.all()


class ListTeacherView(ListAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = ListTeacherSerializer
    queryset = Teacher.objects.all()
