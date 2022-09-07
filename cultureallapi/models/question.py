from django.db import models

class Question(models.Model):
    question_text = models.TextField(max_length=100)
    question_type = models.ForeignKey("QuestionType", on_delete=models.CASCADE, related_name="question_type_id")