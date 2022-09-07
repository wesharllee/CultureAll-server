import imp
from django.db import models

class UserQuestionType(models.Model):
    cult_user = models.ForeignKey("CultUser", on_delete=models.CASCADE)
    question_type = models.ForeignKey("QuestionType", on_delete=models.CASCADE)