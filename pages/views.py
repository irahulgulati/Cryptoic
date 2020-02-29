from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
	# return HttpResponse("<h1>Hello World</h1>")
	return render(request,"home.html", {})

def contact_view(request, *args, **kwargs):
	my_contact = {
		"my_text": "lala",
		"my_list": [123,242,54564]
				  }
	return render(request,"contact.html", my_contact)
