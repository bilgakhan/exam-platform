# Generated by Django 4.1.4 on 2022-12-14 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'fan', 'verbose_name_plural': 'fanlar'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'savol', 'verbose_name_plural': 'savollar'},
        ),
        migrations.AddField(
            model_name='question',
            name='image_link',
            field=models.URLField(blank=True, null=True, verbose_name='rasm havolasi'),
        ),
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='saqlangan vaqti'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='nomi'),
        ),
        migrations.AlterField(
            model_name='course',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name="o'zgartirilgan vaqti"),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=200, verbose_name='javob'),
        ),
        migrations.AlterField(
            model_name='question',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='courses.course', verbose_name='fan'),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='saqlangan vaqti'),
        ),
        migrations.AlterField(
            model_name='question',
            name='option2',
            field=models.CharField(max_length=200, verbose_name='2-variant'),
        ),
        migrations.AlterField(
            model_name='question',
            name='option3',
            field=models.CharField(max_length=200, verbose_name='3-variant'),
        ),
        migrations.AlterField(
            model_name='question',
            name='option4',
            field=models.CharField(max_length=200, verbose_name='4-variant'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=200, verbose_name='savol'),
        ),
        migrations.AlterField(
            model_name='question',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name="o'zgartirilgan vaqti"),
        ),
    ]
