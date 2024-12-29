from courses.models import Group
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from .models import CustomUser, Student, Teacher
from .serializers import (
    CustomUserSerializer,
    StudentSerializer,
    TeacherSerializer,
    TeacherStudentSerializer,
)


class CustomUserViewSetAPI(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class StudentViewSetAPI(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSetAPI(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherStudentListAPIView(ListAPIView):
    serializer_class = TeacherStudentSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Group.objects.filter(pk=pk)
