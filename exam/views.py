from random import shuffle
from django.http import HttpResponseForbidden
from django.db.models.functions import Now
from django.views.generic.base import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.conf import settings
from courses.models import Question
from .models import Exam, ExamQuestion
from .forms import ExamTakeForm, ExamQuestionForm, ExamFinalForm


class ExamHomeView(TemplateView):
    template_name = 'exam/index.html'


class ExamTakeView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        if request.user.balance == 0:
            return render(request, 'exam/insufficient.html')

        context = {
            'form': ExamTakeForm()
        }
        return render(request, 'exam/take.html', context=context)

    def post(self, request, *args, **kwargs):
        take_form = ExamTakeForm(request.POST)
        if take_form.is_valid():
            if request.user.balance == 0:
                return HttpResponseForbidden()
            hour_ago = Now() - settings.EXAM['lifetime']
            last = Exam.objects.filter(student=request.user, started_at__gt=hour_ago).last()
            if last:
                if last.ended_at is None:  # if there is another active exam
                    return redirect('exam-question', question_number=1)
            exam = Exam(
                student=request.user,
                course=take_form.cleaned_data['course'],
            )
            exam.save()
            questions = Question.objects.order_by('?').all()[:settings.EXAM['questions']]
            for (question, i) in zip(questions, range(1, settings.EXAM['questions']+1)):
                options = [question.answer, question.option2, question.option3, question.option4]
                shuffle(options)
                exam_question = ExamQuestion(
                    exam=exam,
                    question=question.question,
                    image_link=question.image_link,
                    answer=question.answer,
                    option1=options[0],
                    option2=options[1],
                    option3=options[2],
                    option4=options[3],
                    number=i,
                )
                exam_question.save()
            request.user.balance -= 1
            request.user.save()
            return redirect('exam-question', question_number=1)
        return redirect('exam-take')


class ExamQuestionView(LoginRequiredMixin, View):
 
    def get(self, request, *args, **kwargs):
        last = Exam.objects.filter(
            student=request.user,
            started_at__gt=Now() - settings.EXAM['lifetime'],
            ended_at=None,
        ).last()
        if not last:
            return redirect('exam-result')
        question = ExamQuestion.objects.filter(exam=last, number=kwargs['question_number']).first()
        form = ExamQuestionForm()
        form.fields['answer'].choices = [
            ('1', question.option1),
            ('2', question.option2),
            ('3', question.option3),
            ('4', question.option4),
        ]
        questions = ExamQuestion.objects.filter(exam=last).all()
        questions = [
            {
                'number': question.number,
                'answered': question.given_answer != None,
            } for question in questions
        ]
        context = {
            'questions': questions,
            'current': question,
            'started_at': last.started_at,
            'form': form,
        }
        return render(request, 'exam/question.html', context=context)

    def post(self, request, *args, **kwargs):
        last = Exam.objects.filter(
            student=request.user,
            started_at__gt=Now() - settings.EXAM['lifetime'],
            ended_at=None
        ).last()
        question_number = kwargs['question_number']
        question = ExamQuestion.objects.filter(exam=last, number=question_number).first()
        if not question:
            return redirect('exam-final')
        questions_count = ExamQuestion.objects.filter(exam=last).count()
        form = ExamQuestionForm(request.POST)
        if form.is_valid():
            match form.cleaned_data['answer']:
                case '1': question.given_answer = question.option1
                case '2': question.given_answer = question.option2
                case '3': question.given_answer = question.option3
                case '4': question.given_answer = question.option4
            question.save()
            if question_number < questions_count:
                return redirect('exam-question', question_number=question_number+1)
            else:
                return redirect('exam-final')
        return redirect('exam-question', question_number=question_number)


class ExamFinalView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        last = Exam.objects.filter(
            student=request.user,
            started_at__gt=Now() - settings.EXAM['lifetime'],
            ended_at=None,
        ).last()
        if last is None:
            return redirect('exam-result')
        form = ExamFinalForm()
        context = {
            'exam': last,
            'form': form,
        }
        return render(request, 'exam/final.html', context=context)

    def post(self, request, *args, **kwargs):
        last = Exam.objects.filter(
            student=request.user,
            started_at__gt=Now() - settings.EXAM['lifetime'],
            ended_at=None,
        ).last()
        if last is None:
            return redirect('exam-result')
        form = ExamFinalForm(request.POST)
        if form.is_valid():
            last.ended_at = Now()
            last.save()
            return redirect('exam-result', id=last.id)
        return redirect('exam-final')


class ExamResultView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        exam_id = kwargs.get('id')
        if exam_id is None:
            last = Exam.objects.filter(
                student=request.user,
            ).last()
            exam_id = last.id
            return redirect('exam-result', id=exam_id)

        exam = Exam.objects.get(id=exam_id)
        context = {
            'exam': exam,
            'questions': [],
        }
        questions = ExamQuestion.objects.filter(exam=exam).order_by('number').all()
        corrects = 0
        for question in questions:
            context['questions'].append({
                'number': question.number,
                'correct': question.given_answer == question.answer
            })
            if question.given_answer == question.answer: corrects += 1
        context['corrects'] = corrects
        context['score'] = corrects * settings.EXAM['answer_score']
        return render(request, 'exam/result.html', context=context)


class ExamHistoryView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        exams = Exam.objects.filter(student=request.user).all()
        context = {'exams': exams}
        return render(request, 'exam/history.html', context=context)


class ExamOverallHistoryView(LoginRequiredMixin, UserPassesTestMixin, View):

    def get(self, request, *args, **kwargs):
        exams = Exam.objects.filter().all()
        context = {'exams': exams}
        return render(request, 'exam/all-history.html', context=context)

    def test_func(self):
        return self.request.user.is_superuser
