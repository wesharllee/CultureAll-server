from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Answer(models.Model):
    question = models.ForeignKey("Question", on_delete=models.CASCADE, related_name="answers")
    rating_value = models.IntegerField(
        default=3,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
        )
    cult_user = models.ForeignKey("CultUser", on_delete=models.CASCADE, related_name="answers")