from django.urls import path
from .views import (
    ExamHomeView,
    ExamTakeView,
    ExamQuestionView,
    ExamFinalView,
    ExamResultView,
    ExamHistoryView,
    ExamOverallHistoryView,
)

urlpatterns = [
    path('', ExamHomeView.as_view(), name='exam-home'),
    path('take/', ExamTakeView.as_view(), name='exam-take'),
    path('questions/<int:question_number>/', ExamQuestionView.as_view(), name='exam-question'),
    path('questions/final/', ExamFinalView.as_view(), name='exam-final'),
    path('result/', ExamResultView.as_view(), name='exam-result'),
    path('result/<int:id>', ExamResultView.as_view(), name='exam-result'),
    path('history/', ExamHistoryView.as_view(), name='exam-history'),
    path('history-all/', ExamOverallHistoryView.as_view(), name='exam-history-all'),
]
