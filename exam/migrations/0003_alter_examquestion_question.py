# Generated by Django 4.1.4 on 2022-12-25 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_alter_exam_options_alter_examquestion_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examquestion',
            name='question',
            field=models.CharField(max_length=1024, verbose_name='savol'),
        ),
    ]