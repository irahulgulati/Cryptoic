from django.db import models
from django.forms import ModelForm
from django.urls import reverse

# Create your models here.
class rsa(models.Model):
	p 			=models.IntegerField(max_length=120)
	q			=models.IntegerField(blank=False,null=False,max_length=120)
	e 			=models.IntegerField(max_length=120)
	m			=models.CharField(max_length=120)

	def get_absolute_url(self):
		return reverse("rsa:rsa",kwargs={"id": self.id})
