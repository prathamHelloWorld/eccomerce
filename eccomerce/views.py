from django.shortcuts import render,redirect
from .forms import AboutForm,LoginForm,RegisterForm
from django.contrib.auth import authenticate,login
from django.contrib.auth import get_user_model
User=get_user_model()
def homePage(request):
    return render(request,template_name="index.html")

def aboutPage(request):
    form=AboutForm(request.POST or None)
    context={
        'form':form
    }
    return render(request,"about.html",context)

def loginPage(request):
    form=LoginForm(request.POST or None)
    context={
        'form':form,
        'error':''
    }
    if form.is_valid():
        context['form']=LoginForm()
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            context['error']='not valid'
    return render(request,"login.html",context)

def registerPage(request):
    form=RegisterForm(request.POST or None)
    context={
        'form':form,
    }
    if form.is_valid():
        context['form']=RegisterForm()
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        email=form.cleaned_data.get('email')
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return redirect('/admin')
    return render(request,"register.html",context)
