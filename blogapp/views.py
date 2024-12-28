from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def index(request):
  posts = Post.objects.all().order_by('-time') 
  return render(request, 'index2.html', {'posts': posts})

def publish(request):
  post = Post.objects.all()

  if request.method == 'POST':
    author = request.POST.get('author')
    title = request.POST.get('title')
    content = request.POST.get('content')
    time = request.POST.get('time')
  
    create = Post.objects.create(author=author, title=title, content=content, time=time)
    create.save()
    return redirect('index')
  
  return render(request, 'publish.html')
    
        
def deletePost(request, pk):
  post = Post.objects.get(pk=pk)
  post.delete()
  return redirect('index')

def updatePost(request, pk):
  post = Post.objects.get(pk=pk)
  
  if request.method == 'POST':
    post.author = request.POST.get('newAuthor')
    post.title = request.POST.get('newTitle')
    post.time = post.modified
    post.content = request.POST.get('newContent')
    post.save()
    return redirect('index')
  return render(request, 'update.html', {'post': post})

def post(request, pk):
  post = Post.objects.get(pk=pk)
  comments = Comment.objects.filter(post=post)

  if request.method == 'POST':
    name = request.POST.get('name')
    body = request.POST.get('body')
    time = request.POST.get('time')
    post = post
    create = Comment.objects.create(name=name, body=body, time=time, post=post)
    create.save()
    return redirect('post', pk=pk)
  
  return render(request, 'post.html', {'post': post, 'comments': comments})
