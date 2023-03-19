from rest_framework import serializers
from rest_framework.reverse import reverse
from authentication.serializers import RegisterSerializer
from authentication.models import User
from .models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = ('id', 'answer', 'question', 'url')

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse('answer-detail', args=[obj.question.id, obj.pk], request=request)


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    url = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('id', 'title', 'Question', 'answers', 'url')

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse('question-detail', args=[obj.pk], request=request)

  

class QuestionDetailSerializer(serializers.HyperlinkedModelSerializer):

    answers_url = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('id', 'title', 'Question',  'answers_url')

    def get_answers_url(self, obj):
        request = self.context.get('request')
        return reverse('answer-list', args=[obj.pk], request=request)



class AnswerDetailSerializer(serializers.ModelSerializer):
    question = serializers.StringRelatedField()
    
    class Meta:
        model = Answer
        fields = ('id', 'answer', 'question')

