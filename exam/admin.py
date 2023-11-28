from django.contrib import admin
from .models import Exam, ExamQuestion


class ExamQuestionInline(admin.TabularInline):
    model = ExamQuestion
    extra = 0


class ExamAdmin(admin.ModelAdmin):
    inlines = [
        ExamQuestionInline
    ]
    readonly_fields = ('course', 'student', 'ended_at',)


class ExamQuestionAdmin(admin.ModelAdmin):
    readonly_fields = ('exam', 'question', 'number', 'answer', 'given_answer',
        'option1', 'option2', 'option3', 'option4',)


admin.site.register(Exam, ExamAdmin)
admin.site.register(ExamQuestion, ExamQuestionAdmin)
