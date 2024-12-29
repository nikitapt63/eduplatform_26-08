from django.db import models


class Specialization(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = "Специализации"
        verbose_name_plural = "Специализации"
