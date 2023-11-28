from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='nomi')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='saqlangan vaqti')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='o\'zgartirilgan vaqti')

    class Meta:
        verbose_name = 'fan'
        verbose_name_plural = 'fanlar'

    def __str__(self) -> str:
        return self.name


class Question(models.Model):
    question = models.CharField(max_length=1024, verbose_name='savol')
    image_link = models.URLField(blank=True, null=True, verbose_name='rasm havolasi')
    answer = models.CharField(max_length=200, verbose_name='javob')
    option2 = models.CharField(max_length=200, verbose_name='2-variant')
    option3 = models.CharField(max_length=200, verbose_name='3-variant')
    option4 = models.CharField(max_length=200, verbose_name='4-variant')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='questions', verbose_name='fan')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='saqlangan vaqti')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='o\'zgartirilgan vaqti')

    class Meta:
        verbose_name = 'savol'
        verbose_name_plural = 'savollar'

    def __str__(self) -> str:
        return f'{self.course.name} | {self.question}'
