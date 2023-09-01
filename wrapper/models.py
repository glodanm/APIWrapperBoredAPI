from django.db import models


class Activity(models.Model):
    activity = models.CharField(max_length=200)
    type = models.CharField(max_length=50)
    participants = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    accessibility = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.URLField()

    def __str__(self):
        return self.activity
    