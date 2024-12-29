from django.db import models
from django.utils import timezone
from users.models import Student, Teacher

# __all__ = {
#     "Specialization",
#     "Course",
#     "Group",
#     "Topic",
#     "Test",
#     "Question",
#     "Answer",
#     "Article",
#     "CompletedTest",
#     "Image",
# }


class Image(models.Model):
    file = models.ImageField(verbose_name="Файл")

    def __str__(self):
        return f"Image - {self.pk}"

    def get_image_url(self):
        if self.file:
            return self.file.url
        return ""

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"


class Specialization(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = "Специализации"
        verbose_name_plural = "Специализации"


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    duration = models.DurationField(verbose_name="Продолжительность")
    specialization = models.ManyToManyField(Specialization)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Group(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    date_formation = models.DateField(
        verbose_name="Дата образования", default=timezone.now()
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    students = models.ManyToManyField(Student, verbose_name="Студенты")
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, verbose_name="Преподаватель"
    )

    @property
    def students_quantity(self):
        return len(self.students.all())

    def __str__(self):
        return f"{self.pk} - {self.title} - {self.date_formation}"

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class Topic(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"


class Test(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    image = models.ManyToManyField(Image, verbose_name="Фото", blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name="Тема")

    def __str__(self):
        return f"Test #{self.pk} - {self.title}"

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"


class Question(models.Model):
    DIFFICULTY_CHOICES = [
        ("Easy", "Easy"),
        ("Medium", "Medium"),
        ("Hard", "Hard"),
    ]

    text = models.TextField(verbose_name="Текст вопроса")
    difficulty = models.CharField(
        max_length=6, choices=DIFFICULTY_CHOICES, verbose_name="Сложность"
    )
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Тест")

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return f"{self.pk} - {self.text} - {self.difficulty}"


class Answer(models.Model):
    title = models.CharField(max_length=100, verbose_name="Ответ")
    is_correct = models.BooleanField(verbose_name="Верный ответ")
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name="Вопрос"
    )

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    def __str__(self):
        return f"{self.pk} - {self.title}"


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ManyToManyField(Image, verbose_name="Фото", blank=True)
    specializations = models.ManyToManyField(Specialization)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class CompletedTest(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} - {self.test}"

    class Meta:
        verbose_name = "Выполненный тест"
        verbose_name_plural = "Выполненные тесты"
