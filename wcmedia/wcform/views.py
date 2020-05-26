from django.shortcuts import render
from django.http import HttpResponse
from .models import UserInfo
from .forms import UserInfoForm
# Create your views here.



def viewfield(request):
    context = {}
    
    if request.method == 'POST':
        form = UserInfoForm(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Success')
        else:
            print(form.errors)
        
    else:
        form = UserInfoForm()
    return render(request, 'wcform/register.html', {'form' : form})

            