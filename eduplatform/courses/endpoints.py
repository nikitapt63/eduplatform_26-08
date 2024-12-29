from django.db.models import Q, Subquery
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from users.models import Student, Teacher
from users.serializers import StudentSerializer, TeacherSerializer

from .models import (
    Answer,
    Article,
    CompletedTest,
    Course,
    Group,
    Image,
    Question,
    Specialization,
    Test,
    Topic,
)
from .serializers import (
    AnswerSerializer,
    ArticleSerializer,
    CompletedTestSerializer,
    CourseSerializer,
    GroupSerializer,
    ImageSerializer,
    QuestionSerializer,
    SpecializationSerializer,
    TestSerializer,
    TopicSerializer,
)


class SpecializationViewsetAPI(ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class CourseViewsetAPI(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class GroupViewsetAPI(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TopicViewsetAPI(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TestViewsetAPI(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class QuestionViewsetAPI(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewsetAPI(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class ArticleViewsetAPI(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CompletedTestViewsetAPI(ModelViewSet):
    queryset = CompletedTest.objects.all()
    serializer_class = CompletedTestSerializer


class ImageViewSetAPI(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class StudentCoursesListAPIView(ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        student = get_object_or_404(Student, pk=pk)
        groups = student.groups.all()
        return [group.course for group in groups]


class GroupStudentListAPIView(ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        group = get_object_or_404(Group, pk=pk)
        return Student.objects.filter(group=group).all()


class TeacherRecommendationListAPIView(ListAPIView):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        course = get_object_or_404(Course, pk=pk)
        course_specializations = course.specialization.all()
        rec_teachers = Teacher.objects.filter(
            specializations__in=course_specializations
        ).distinct()
        return rec_teachers


class CourseRecommendationListAPIView(ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        student_courses = Course.objects.filter(group__students__pk=pk).values("pk")
        student_specializations = Specialization.objects.filter(
            course__in=Subquery(student_courses)
        ).values("pk")
        rec_courses = Course.objects.filter(
            Q(specialization__in=Subquery(student_specializations))
            & ~Q(group__students__pk=pk)
        ).distinct()
        return rec_courses
