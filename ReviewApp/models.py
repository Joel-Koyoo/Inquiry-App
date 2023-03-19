from django.db import models
from authentication.models import User
from helpers.models import TrackingModel

# Create your models here.


class Question(TrackingModel):
    title = models.CharField(max_length=255)
    Question = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_at',)  # Order by the 'created_at' field

    def __str__(self):
        return f'{self.Question}' 

class Answer(models.Model):
    answer = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.answer}'

 