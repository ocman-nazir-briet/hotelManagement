from operator import iconcat
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from datetime import datetime
from .models import *
from .forms import *
def profile(request):
    obj = clients.objects.all()
    return render(request, 'profile.html', {'obj':obj})

def dashboard(request):
    if request.user.is_anonymous:
        return redirect("/login")
    clients_objects = clients.objects.all()
    clientCount = clients_objects.count()
    staff_objects = staff.objects.all()
    staffCount = staff_objects.count()
    food_objects = food.objects.all()
    foodCount = food_objects.count()
    branch_objects=branch.objects.all()
    branchCount = branch_objects.count()
    order_objects = orders.objects.all()
    
    context = {'clientCount':clientCount, 'clients_objects':clients_objects, 'staff_objects':staff_objects, 
    'staffCount':staffCount, 'food_objects':food_objects, 'foodCount':foodCount, 'branch_objects':branch_objects,'branchCount':branchCount, 'order_objects':order_objects}
    
    return render(request, 'dashboard.html', context)

def clientAdd(request):
    if request.method == "POST":
        form = clientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = clientForm()
    client = clients.objects.all()
    return render(request, 'adder/clientAdd.html', {'client':client,'form':form})

def staffAdd(request):
    if request.method == "POST":
        form = staffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = staffForm()
    staffs = staff.objects.all()
    return render(request, 'adder/staffAdd.html', {'staff':staffs, 'form':form})

def foodAdd(request):
    if request.method== "POSt":
        form = foodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/foodAdd')
    form = foodForm
    foods = food.objects.all()
    return render(request, 'adder/foodAdd.html',{'form':form, 'foods':foods})

def branchAdd(request):
    if request.method == "POST":
        form = branchAdd(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/branchAdd')
    form = branchForm
    branches = branch.objects.all()
    return render(request, 'adder/branchAdd.html', {'form':form, 'branches':branches})


def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('usernam')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/dashboard")
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")