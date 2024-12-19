from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from . forms import CreateTaskForm
from . models import Task
from django.http import JsonResponse

def home(request): 
    return render(request, 'home.html')
 
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
  
def login_user(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

@login_required 
def profile(request): 
    tasks = Task.objects.filter(user=request.user)
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/profile")
    context = {'tasks':tasks}
    return render(request, 'profile.html',context=context)
  
def logout_user(request):
    logout(request)
    return redirect('/')


def create_task(request):
    if request.method == 'POST':
        title =  request.POST['bt1']
        description =  request.POST['bt2']
        start =  request.POST['bt3']
        end =  request.POST['bt4']
        task = Task(title=title,description=description,start_date=start,end_date = end,user=request.user)
        task.save()
        return redirect('/profile')
    return render(request,'create_task.html')


def delete_task(request,taskid):
    task = Task.objects.get(id=taskid)
    task.delete()
    return redirect('/profile')


def edit_task(request,taskid):
    
    print(taskid)
    if request.method == 'POST':
        title =  request.POST['bt1']
        description =  request.POST['bt2']
        start =  request.POST['bt3']
        end =  request.POST['bt4']
        task  =Task.objects.get(id=taskid)
        task.title = title
        task.description = description
        if start:
            print("start")
            task.start_date = start
        if end:
            task.end_date = end
        task.save()
        return redirect('/profile')
    task = Task.objects.get(id=taskid)
    return render(request,'edit_task.html',{'task':task})
