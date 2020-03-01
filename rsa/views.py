from django.shortcuts import render, get_object_or_404
from .models import rsa
from .forms import rsaForm
from .compute import compute
# Create your views here.
def input_values_view(request):
	result = []
	x=None
	y=None
	form=rsaForm(request.POST or None)
	if form.is_valid():
		form2	=form.save(commit=False)
		if 'encrypt' in request.POST:	
			encrypt=1
			result	=compute(encrypt,form2.p, form2.q, form2.e, form2.m)
			x=result["plain"]
			y=result["crypted"]
		else:
			result = "Please encrypt before decrypting"
	context={
		'form':form,
		'result':result,
		'plaintext':x,
		'ciphertext':y
				}
	return render(request, "rsa/input.html",context)