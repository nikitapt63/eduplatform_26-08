from courses.models import Group
from rest_framework.serializers import ModelSerializer, Serializer

from .models import CustomUser, Student, Teacher


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class TeacherStudentSerializer(Serializer):
    teacher = TeacherSerializer()
    students = StudentSerializer(many=True)

    class Meta:
        model = Group
        fields = "__all__"