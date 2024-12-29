from django.contrib import admin

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

admin.site.register(Specialization)
admin.site.register(Course)
admin.site.register(Group)
admin.site.register(Topic)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(CompletedTest)
admin.site.register(Article)
admin.site.register(Answer)
admin.site.register(Image)
