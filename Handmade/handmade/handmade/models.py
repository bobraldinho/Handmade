from django.db import models

class faq_question(models.Model):

	question_text = models.CharField(max_length=200)
	

class faq_answer(models.Model):

	question = models.ForeignKey(faq_question)
	answer_text = models.CharField(max_length = 300)
	