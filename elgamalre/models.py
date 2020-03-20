from django.db import models

# Create your models here.
# Create your models here.
class elgamalre(models.Model):
    pr      =models.IntegerField(blank=False,null=False)
    m       =models.IntegerField(blank=False,null=False)
    rand1   =models.IntegerField(blank=False,null=False)
    rand2   =models.IntegerField(blank=False,null=False)
