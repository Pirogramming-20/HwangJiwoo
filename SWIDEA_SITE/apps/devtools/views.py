from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def devtools_list(request):
    devtools = Devtool.objects.all()
    ctx = {
        'devtools': devtools
    }
    return render(request, 'devtools/devtool_list.html', ctx)

def devtools_create(request):
    if request.method == 'GET':
        form = DevtoolForm()
        ctx = {
            'form': form
        }
        return render(request, 'devtools/devtool_create.html', ctx)
    form = DevtoolForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('devtools:list')

def devtools_detail(request, pk):
    devtool = Devtool.objects.get(id=pk)
    all_idea = devtool.idea.all()
    ctx = {
        'devtool': devtool,
        'all_idea': all_idea
    }
    return render(request, 'devtools/devtool_detail.html', ctx)

def devtools_delete(request, pk):
    if request.method == 'POST':
        devtool = Devtool.objects.get(id=pk)
        devtool.delete()
    return redirect("devtools:list")

def devtools_update(request, pk):
    devtool = Devtool.objects.get(id=pk)
    if request.method == 'GET':
        form = DevtoolForm(instance=devtool)
        ctx = {
            'form': form,
            'pk': pk
        }
        return render(request, 'devtools/devtool_update.html', ctx)
    form = DevtoolForm(request.POST, instance=devtool)
    if form.is_valid():
        form.save()
    return redirect('devtools:detail', pk)