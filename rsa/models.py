from django.db import models
from django.forms import ModelForm
from django.urls import reverse

# Create your models here.
class rsa(models.Model):
	p 			=models.IntegerField(blank=False)
	q			=models.IntegerField(blank=False)
	e 			=models.IntegerField(blank=False)
	m			=models.CharField(max_length=120)

	def get_absolute_url(self):
		return reverse("rsa:rsa",kwargs={"id": self.id})
