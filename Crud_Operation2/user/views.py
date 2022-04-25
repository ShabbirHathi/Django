from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm
from django.urls import reverse_lazy


# Create your views here.

def listview(request):

    user = User.objects.all()
    context = {
        'data': user,
    }
    return render(request, 'list.html', context)


def createview(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('List')

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def editview(request, pk):
    
    user = User.objects.get(id=pk)
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('List')

    context = {
        'data': user,
        'form': form,
    }
    return render(request, 'edit.html', context)


def deleteview(request,pk):
    

    user = User.objects.filter(id=pk)
    
    if request.method == 'POST':
        user.delete()
        return redirect('List')

    context = {
        'data': user,
    }
    return render(request, 'delete.html', context)
