from django.urls import include, path
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
    TopicViewsetAPI,
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
]
