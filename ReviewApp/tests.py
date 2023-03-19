from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


# Create your tests here.


class TestListQuestionAPIView(APITestCase):

    def test_creates_question(self):
        sample_question = {
            "title": "Assignment",
            "Question": "what is one plus one",
            "url": "http://127.0.0.1:8000/inquiry/Questions/1/"
        }
        response = self.client.post(reverse('question-list'), sample_question)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
