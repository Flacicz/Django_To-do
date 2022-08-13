from django.db import models


class Tasks(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=150)
    created_at = models.TimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Список дел'
        verbose_name_plural = 'Список дел'
        ordering = ['-created_at']
