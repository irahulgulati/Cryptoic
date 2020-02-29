from django.shortcuts import render, get_object_or_404
from .models import rsa
from .forms import rsaForm
from .compute import compute,decrypt
# Create your views here.
new = None
def input_values_view(request):
	result = []
	global new
	form=rsaForm(request.POST or None)
	if form.is_valid():
		form2	=form.save(commit=False)
		if 'encrypt' in request.POST:	
			encrypt=1
			new= result	=compute(encrypt,form2.p, form2.q, form2.e, form2.m)
		elif 'decrypt' in request.POST:
			decrypt=2
			result = compute(decrypt,form2.p, form2.q, form2.e, new)
	context={
		'form':form,
		'result':result
				}
	return render(request, "rsa/input.html",context)