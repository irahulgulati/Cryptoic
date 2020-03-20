from django.db import models

# Create your models here.

class elgamaluni(models.Model):
    pr      =models.IntegerField(blank=False)
    m       =models.IntegerField(blank=False)
    rand1   =models.IntegerField(blank=False)
    rand2   =models.IntegerField(blank=False)
