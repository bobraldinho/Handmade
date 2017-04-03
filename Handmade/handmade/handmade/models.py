from django.db import models


class FaqQuestion(models.Model):
    question_text = models.CharField(max_length=200)


class FaqAnswer(models.Model):
    question = models.ForeignKey(FaqQuestion)
    answer_text = models.CharField(max_length=300)
