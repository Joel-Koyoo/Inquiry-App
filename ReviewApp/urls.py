from django.urls import path
from django.contrib import admin
from ReviewApp.views import QuestionAPIView, QuestionDetailAPIView, AnswerAPIView, AnswerDetailAPIView


urlpatterns = [
    path('Questions/', QuestionAPIView.as_view(), name='vx'),
    path('Questions/<int:id>/', QuestionDetailAPIView.as_view(), name='question-detail'),
    path('Questions/<int:id>/answers/', AnswerAPIView.as_view(), name='answer-list'),
    path('Questions/<int:id>/answers/<int:pk>/', AnswerDetailAPIView.as_view(), name='answer-detail'),
]       