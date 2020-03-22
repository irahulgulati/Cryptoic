from django import forms
from .models import elgamalre

class elgamalreForm(forms.ModelForm):
	pr 		    = 		forms.IntegerField(label='Private Key x, x ',widget=forms.TextInput(attrs={
					'placeholder':'Enter first private key',
					'class': 		'form-control',


					}))
	m 		    = 		forms.IntegerField(label='Message, m ',widget=forms.TextInput(attrs={"placeholder":"Enter message to be encrypted",
										'class': 		'form-control',
										}))
	rand1 		= 		forms.IntegerField(label='Random Number, r',widget=forms.TextInput(attrs={"placeholder":"Enter first random number",
										'class': 		'form-control',
										}))
	rand2 		=		forms.CharField(label='Random Number, r1',widget=forms.TextInput(attrs={"placeholder":"Enter second random number",
									'class': 		'form-control',
									}))
	class Meta:
		model = elgamalre
		fields = [
			'pr',
			'm',
			'rand1',
			'rand2'

				]