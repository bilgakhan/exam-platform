from django import forms
from .models import Exam


class ExamTakeForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ('course',)


class ExamQuestionForm(forms.Form):
    options = [
        ('1', 'Option 1'),
        ('2', 'Option 2'),
        ('3', 'Option 3'),
        ('4', 'Option 4'),
    ]
    answer = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=options,
        required=False,
    )


class ExamFinalForm(forms.Form):
    pass
