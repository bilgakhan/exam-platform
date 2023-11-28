from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
from courses.models import Course, Question


class Exam(models.Model):
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='exams')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='exams', verbose_name='fan')
    started_at = models.DateTimeField(auto_now_add=True, verbose_name='boshlangan vaqti')
    ended_at = models.DateTimeField(blank=True, null=True, verbose_name='tugagan vaqti')

    class Meta:
        verbose_name = 'imtihon'
        verbose_name_plural = 'imtihonlar'

    def __str__(self) -> str:
        return f'{self.course.name} | {self.student.username}'


class ExamQuestion(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions', verbose_name='imtihon')
    question = models.CharField(max_length=1024, verbose_name='savol')
    image_link = models.URLField(blank=True, null=True, verbose_name='rasm havolasi')
    number = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100),
        ],
        verbose_name='tartib raqami'
    )
    answer = models.CharField(max_length=200, verbose_name='javob')
    given_answer = models.CharField(max_length=200, blank=True, null=True, verbose_name='berilgan javob')
    option1 = models.CharField(max_length=200, verbose_name='1-variant')
    option2 = models.CharField(max_length=200, verbose_name='2-variant')
    option3 = models.CharField(max_length=200, verbose_name='3-variant')
    option4 = models.CharField(max_length=200, verbose_name='4-variant')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='o\'zgartiligan vaqti')
    
    class Meta:
        verbose_name = 'imtihon savoli'
        verbose_name_plural = 'imtihon savollari'

    def __str__(self) -> str:
        return f'{self.exam.course.name} | {self.exam.student.username} | {self.question}'
