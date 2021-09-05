from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from .serializers import DetailStudentSerializer
from .models import Student
from .serializers import CreateStudentSerializer, ListStudentSerializer


# Class based view is used
# Create new student by teacher or admin
class CreateStudentView(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = CreateStudentSerializer
    queryset = Student.objects.all()


# List all students by teacher or admin
class ListStudentView(ListAPIView):
    serializer_class = ListStudentSerializer
    permission_classes = [IsAdminUser]
    queryset = Student.objects.all()


# Student can see only her/him details.
class DetailStudentView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DetailStudentSerializer

    def get_object(self):
        return Student.objects.get(user=self.request.user)
