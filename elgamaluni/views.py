from django.shortcuts import render
from .models import elgamaluni
from .forms import elgamaluniform
from .compute import compute

def input_values_view(request):
    result=[]
    form = elgamaluniform(request.POST or None)
    if form.is_valid():
        form2=form.save(commit=False)
        if 'encrypt' in request.POST:
            result  =   compute(form2.pr,form2.m,form2.rand1,form2.rand2)
        else:
            result = "Something went wrong"
    context = {
        'form'     :   form,
        'result'   :    result 
    }

    return render(request, "elgamaluni/input.html",context)
