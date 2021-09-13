from django.db import models

# Create your models here.


class course(models.Model):
    name = models.CharField(max_length=200)
    semeter = models.IntegerField()
    year = models.IntegerField()
    seat = models.IntegerField()