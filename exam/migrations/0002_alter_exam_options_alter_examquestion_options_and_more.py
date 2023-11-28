# Generated by Django 4.1.4 on 2022-12-14 13:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_options_alter_question_options_and_more'),
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={'verbose_name': 'imtihon', 'verbose_name_plural': 'imtihonlar'},
        ),
        migrations.AlterModelOptions(
            name='examquestion',
            options={'verbose_name': 'imtihon savoli', 'verbose_name_plural': 'imtihon savollari'},
        ),
        migrations.AddField(
            model_name='examquestion',
            name='image_link',
            field=models.URLField(blank=True, null=True, verbose_name='rasm havolasi'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='courses.course', verbose_name='fan'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='ended_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='tugagan vaqti'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='started_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='boshlangan vaqti'),
        ),
        migrations.AlterField(
            model_name='examquestion',
            name='answer',
            field=models.CharField(max_length=200, verbose_name='javob'),
        ),
        migrations.AlterField(
            model_name='examquestion',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti'),
        ),
        migrations.AlterField(
            model_name='examquestion',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='exam.exam', verbose_name='imtihon'),
        ),
        migrations.AlterField(
            model_name='examquestion',
            name='given_answer',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='berilgan javob'),
        ),
        migrations.AlterField(
            model_name='examquestion',
            name='number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='tartib raqami'),
        ),
        migrations.AlterField(
            model_name='examquestion',
            name='option1',
            field=models.CharField(max_length=200, verbose_name='1-variant'),
        ),
        migrations.AlterField(
            model_name='examquestion',
            name='option2',
            field=models.CharField(max_length=200, verbose_name='2-variant'),
        ),
        migrations.AlterField(
            model_name='examquestion',
            name='option3',
            field=models.CharField(max_length=200, verbose_name='3-variant'),
        ),
        migrations.AlterField(
            model_name='examquestion',
            name='option4',
            field=models.CharField(max_length=200, verbose_name='4-variant'),
        ),
        migrations.AlterField(
            model_name='examquestion',
            name='question',
            field=models.CharField(max_length=500, verbose_name='savol'),
        ),
        migrations.AlterField(
            model_name='examquestion',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name="o'zgartiligan vaqti"),
        ),
    ]
