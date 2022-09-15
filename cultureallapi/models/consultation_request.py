from django.db import models

class ConsultationRequest(models.Model):
    cult_user = models.ForeignKey("CultUser", on_delete=models.CASCADE, related_name="consultation")
    date = models.DateField()
    time = models.TimeField()
    in_person = models.BooleanField()
    address = models.CharField(max_length=50,null=True)
    completed = models.BooleanField(False)

    @property
    def readable_time(self):
        return self.time.strftime("%I:%M %p")

    @property
    def readable_date(self):
        return self.date.strftime("%b %d, %Y")
