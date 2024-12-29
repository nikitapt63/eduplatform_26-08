from django.urls import include, path, re_path
from rest_framework.routers import SimpleRouter

from .endpoints import (
    AnswerViewsetAPI,
    ArticleViewsetAPI,
    CompletedTestViewsetAPI,
    CourseViewsetAPI,
    GroupViewsetAPI,
    ImageViewSetAPI,
    QuestionViewsetAPI,
    SpecializationViewsetAPI,
    TestViewsetAPI,
    TopicViewsetAPI, StudentCoursesListAPIView, GroupStudentListAPIView, TeacherRecommendationListAPIView,
    CourseRecommendationListAPIView,
)

router = SimpleRouter()
router.register("specializations", SpecializationViewsetAPI)
router.register("courses", CourseViewsetAPI)
router.register("groups", GroupViewsetAPI)
router.register("topics", TopicViewsetAPI)
router.register("tests", TestViewsetAPI)
router.register("questions", QuestionViewsetAPI)
router.register("answers", AnswerViewsetAPI)
router.register("articles", ArticleViewsetAPI)
router.register("completed_tests", CompletedTestViewsetAPI)
router.register("images", ImageViewSetAPI)


urlpatterns = [
    path("", include(router.urls)),
    re_path("student-courses/(?P<pk>[^/.]+)/", StudentCoursesListAPIView.as_view()),
    re_path("group/(?P<pk>[^/.]+)/", GroupStudentListAPIView.as_view()),
    re_path(
        "course/(?P<pk>[^/.]+)/recommendations/",
        TeacherRecommendationListAPIView.as_view(),
    ),
    re_path(
        "student/(?P<pk>[^/.]+)/recommendations/",
        CourseRecommendationListAPIView.as_view(),
    ),
]