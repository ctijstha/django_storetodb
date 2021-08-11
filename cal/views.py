from django.shortcuts import render
from django.http import HttpResponse
from cal.forms import InformationForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = InformationForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse("Information successfully stored in database" )
            
    else:
        form = InformationForm()
    return render(request,'home.html',{'form':form})




