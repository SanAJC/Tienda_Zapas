from django.shortcuts import render ,redirect
from .forms import RegistartionForm
from django.contrib import messages , auth 
from django.contrib.auth import logout
# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegistartionForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('Inicio')
        else:
            messages.error(request, form.errors)
    else:
        form = RegistartionForm()
        

    context={
        'form':form,
    }
    return render(request,'pages/register.html',context)

def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']

        user=auth.authenticate(email=email,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('Inicio')
        else:
            messages.error(request,'Credenciales incorrectas')
            return redirect('login')
        
    return render(request,'pages/login.html')

def logout_view(request):
    logout(request)
    return redirect('Inicio')
