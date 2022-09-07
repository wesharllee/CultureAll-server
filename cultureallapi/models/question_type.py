from django.db import models


class QuestionType(models.Model):
    type = models.CharField(max_length=20)
    companies = models.ManyToManyField("CultUser", through="UserQuestionType", related_name="question_types")


    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value