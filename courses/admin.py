from django.contrib import admin
from .models import Course, Question


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline
    ]


admin.site.register(Course, CourseAdmin)
admin.site.register(Question)
