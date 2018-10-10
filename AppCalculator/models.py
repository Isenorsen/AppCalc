from django.db import models

# Create your models here.

class PartOfApp(models.Model):
    part = models.CharField(max_length=150)
    fee = models.CharField(max_length=150)

    def __str__(self):
        return self.part


