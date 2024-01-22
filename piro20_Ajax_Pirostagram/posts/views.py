from django.shortcuts import render, redirect
from .models import *
from .forms import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    ctx = {
        "posts": posts,
        "comments": comments,
    }
    return render(request, 'posts/post_list.html', ctx)

def post_create(request):
    if request.method == "GET":
        form = PostForm()
        ctx = {
            "form": form,
        }
        return render(request, "posts/post_create.html", ctx)
    form = PostForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('post:list')

@csrf_exempt
def post_like(request):
    req = json.loads(request.body)
    post_id = req['id']

    post = Post.objects.get(id=post_id)
    post.like += 1

    post.save()

    return JsonResponse({'id': post_id, 'like': post.like}) 

@csrf_exempt
def post_comment(request):
    req = json.loads(request.body)
    post_id = req['id']
    post = Post.objects.get(id=post_id)

    comment_content = req['comment']
    comment = Comment.objects.create(post=post, content=comment_content)
    return JsonResponse({'id': post_id, 'comment': comment.content, 'comment_id': comment.id})

@csrf_exempt
def comment_delete(request):
    req = json.loads(request.body)
    comment_id = req['id']
    comment = Comment.objects.get(id=comment_id)

    comment.delete()
    return JsonResponse({'id': comment_id})

@csrf_exempt
def post_delete(request):
    req = json.loads(request.body)
    post_id = req['id']
    post = Post.objects.get(id=post_id)
    post.delete()
    return JsonResponse({'id': post_id})