from django.shortcuts import render, get_object_or_404
from .models import elgamalre
from .forms import elgamalreForm
from .compute import compute

def input_value_view(request):
    result=[]
    x=None
    y=None
    form = elgamalreForm(request.POST or None)
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

    return render(request, "elgamalre/input.html",context)

