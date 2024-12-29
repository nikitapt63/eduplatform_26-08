from rest_framework.viewsets import ModelViewSet

from .models import CustomUser, Student, Teacher
from .serializers import CustomUserSerializer, StudentSerializer, TeacherSerializer


class CustomUserViewSetAPI(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class StudentViewSetAPI(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSetAPI(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
