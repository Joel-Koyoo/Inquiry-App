from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Question, Answer
from .serializers import QuestionSerializer, QuestionDetailSerializer, AnswerSerializer, AnswerDetailSerializer


class QuestionAPIView(ListCreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Question.objects.filter(user=self.request.user)


class QuestionDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionDetailSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return Question.objects.filter(user=self.request.user)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['question'] = self.get_object()
        return context


class AnswerAPIView(ListCreateAPIView):
    serializer_class = AnswerSerializer
    lookup_field = 'id'
    
    def perform_create(self, serializer):
        question_id = self.kwargs.get('id')
        question = Question.objects.get(id=question_id)
        user = self.request.user
        answer = serializer.save(user=user, question=question)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['question_id'] = self.kwargs.get('question_id')
        return context

    
    def get_queryset(self):
        user = self.request.user
        question_id = self.kwargs.get('id')
        return Answer.objects.filter(user=user, question_id=question_id)


class AnswerDetailAPIView(RetrieveAPIView):
    serializer_class = AnswerDetailSerializer

    def get_queryset(self):
        question_id = self.kwargs.get('id')
        answer_id = self.kwargs.get('pk')
        return Answer.objects.filter(question_id=question_id, id=answer_id)