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


class TeacherStudentSerializer(ModelSerializer):
    teacher = TeacherSerializer()
    students = StudentSerializer(many=True)

    class Meta:
        model = Group
        fields = ["teacher", "students"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        match instance:
            case Teacher():
                representation["teacher"] = TeacherSerializer(instance.teacher).data
            case Student():
                representation["students"] = StudentSerializer(
                    instance.students.all(), many=True
                ).data
            case _:
                representation["details"] = "Unknown instance type"
        return representation