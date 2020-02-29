from django import forms
from .models import rsa

class rsaForm(forms.ModelForm):
	p 		= 		forms.IntegerField(label='p',widget=forms.TextInput(attrs={
					'placeholder':'Enter first prime number',
					'class': 		'form-control',
					'aria-label':	'Username',


					}))
	q 		= 		forms.IntegerField(label='q',widget=forms.TextInput(attrs={"placeholder":"Enter second prime number",
										'class': 		'form-control',
										}))
	e 		= 		forms.IntegerField(label='e',widget=forms.TextInput(attrs={"placeholder":"Set a public key",
										'class': 		'form-control',
										}))
	m 		=		forms.CharField(label='m',widget=forms.TextInput(attrs={"placeholder":"Input a message",
									'class': 		'form-control',
									}))
	class Meta:
		model = rsa
		fields = [
			'p',
			'q',
			'e',
			'm'

				]
	def clean_q(self,*args,**kwargs):
		q = self.cleaned_data.get("q")
		if q < 7:
			raise forms.ValidationError("Please enter second prime number greater that 7")
		return q