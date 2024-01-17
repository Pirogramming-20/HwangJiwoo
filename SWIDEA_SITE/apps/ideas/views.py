from django.shortcuts import render, redirect
from .models import *
from .forms import IdeaForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Create your views here.
def main(request):
    ideas = Idea.objects.all()
    idea_stars = IdeaStar.objects.all()
    ctx = {
        "ideas": ideas,
        "idea_stars": idea_stars
    }
    return render(request, 'ideas/idea_list.html', ctx)

def create(request):
    if request.method == 'GET':
        form = IdeaForm()
        ctx = {
            'form': form
        }
        return render(request, 'ideas/idea_create.html', ctx)
    
    form = IdeaForm(request.POST, request.FILES)
    if form.is_valid():
        idea = form.save()
        return redirect("ideas:detail", pk=idea.pk)
    return render(request, 'ideas/idea_create.html', {'form': form})

def detail(request, pk):
    idea = Idea.objects.get(id=pk)
    idea_stars = IdeaStar.objects.all()
    idea_star = idea_stars.filter(idea_id=pk).first
    
    ctx = {
        'idea': idea,
        'idea_star': idea_star,
    }
    return render(request, 'ideas/idea_detail.html', ctx)

def delete(request, pk):
    if request.method == "POST":
        idea = Idea.objects.get(id=pk)
        idea.delete()
    return redirect("ideas:main")

def update(request, pk):
    idea = Idea.objects.get(id=pk)
    if request.method == "GET":
        form = IdeaForm(instance=idea)
        ctx = {
            'form': form,
            'pk': pk
        }
        return render(request, 'ideas/idea_update.html', ctx)
    form = IdeaForm(request.POST, request.FILES, instance=idea)
    if form.is_valid():
        form.save()
    return redirect("ideas:detail", pk)

def update_interest(request):
    idea_id = request.POST.get('idea_id')
    action = request.POST.get('action')

    try:
        idea = Idea.objects.get(id=idea_id)
        if action == 'plus':
            idea.interest += 1
        elif action == 'minus' and idea.interest > 0:
            idea.interest -= 1
        idea.save()

        return JsonResponse({'success': True, 'new_interest': idea.interest})
    except Exception as e:
        print(e)
        return JsonResponse({'success': False})
    
def update_star(request, pk):
    idea_star = IdeaStar.objects.get(id=pk)
    if idea_star.star == True:
        idea_star.star = False
    else:
        idea_star.star = True
    idea_star.save()
    return redirect("ideas:main")

def update_star2(request, pk):
    idea_star = IdeaStar.objects.get(id=pk)
    if idea_star.star == True:
        idea_star.star = False
    else:
        idea_star.star = True
    idea_star.save()
    return redirect("ideas:detail", idea_star.idea_id)