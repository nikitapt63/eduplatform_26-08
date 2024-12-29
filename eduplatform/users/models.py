from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(
        max_length=20,
        choices=[
            ('teacher', 'Teacher'),
            ('student', 'Student'),
            ('admin', 'Admin'),
            ('moderator', 'Moderator'),
        ],
        default='student'
    )

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.pk} - {self.email}"

    def __repr__(self):
        return f"{self.pk} - {self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Student(models.Model):
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="Рейтинг",
        default=0,
    )
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь"
    )

    def __str__(self):
        return f"{self.pk} - student {self.user.email}"

    class Meta:
        verbose_name = "Студенты"
        verbose_name_plural = "Студенты"


class Teacher(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    specializations = models.ManyToManyField(
        "courses.Specialization", verbose_name="Специализации"
    )

    def __str__(self):
        return f"{self.pk} - teacher {self.user.email}"

    class Meta:
        verbose_name = "Преподаватели"
        verbose_name_plural = "Преподаватели"