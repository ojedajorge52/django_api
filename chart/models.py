from django.db import models

class Chart(models.Model):
    id = models.AutoField (max_length=50, primary_key=True)
    country = models.CharField(max_length=30)
    currency = models.CharField(max_length=20)
    payment = models.PositiveIntegerField()

    def __str__(self):
        return self.country