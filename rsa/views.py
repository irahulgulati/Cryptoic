from django.shortcuts import render, get_object_or_404
from .models import rsa
from .forms import rsaForm
from .compute import compute,decrypt
# Create your views here.
new = None
val = 0
def input_values_view(request):
	result = []
	global new, val
	form=rsaForm(request.POST or None)
	if form.is_valid():
		form2	=form.save(commit=False)
		if 'encrypt' in request.POST:	
			encrypt=1
			val=1
			new= result	=compute(encrypt,form2.p, form2.q, form2.e, form2.m)
		elif 'decrypt' in request.POST and val >= 1:
			decrypt=2
			result = compute(decrypt,form2.p, form2.q, form2.e, new)
			val = 0
			new = None
		else:
			result = "Please encrypt before decrypting"
	context={
		'form':form,
		'result':result
				}
	return render(request, "rsa/input.html",context)