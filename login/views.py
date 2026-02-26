from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib.auth import login ,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm,LoginForms
from .models import loginm

def registerv(request):
    if request.method == "POST":
        form= LoginForm(request.POST)
        if form.is_valid():
            loginm.objects.create(
                username=form.cleaned_data['username'],
                phone=form.cleaned_data['phone'],
                password=form.cleaned_data['password']
            )
            return redirect('base')   # home pa
            
            
        
    else:
        form=LoginForm(request.POST)
    return render(request,'pauth/register.html',{'form':form})
def loginv(request):
    form = LoginForms()

    if request.method == "POST":
        LoginForms(request.POST)
        if form.is_valid():
            user = loginm.objects.create(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            user.save()
            return redirect('base')

            # if user:
            #     login(request, user)
            #     return redirect('base')
    
        else:
            return redirect("registerv")
    
    return render(request,"pauth/login.html")



# Create your views here.
