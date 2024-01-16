from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Well(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='well/', verbose_name='превью', **NULLABLE)
    documentation = models.URLField(max_length=200, verbose_name='ссылка на документацию')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='lesson/', verbose_name='превью', **NULLABLE)
    video_url = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    well = models.ForeignKey(Well, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE,
                             related_name='lessons')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
