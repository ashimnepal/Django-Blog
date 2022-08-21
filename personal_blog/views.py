from time import timezone
from django.shortcuts import render
from .models import Post
from django.http import HttpResponseRedirect
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
    #posts = Post.objects.all()
    return render (
        request,
        "post_list.html",
        {"posts":posts},
    )

def post_detail(request, pk):
    #post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post,pk=pk)
    return render (
        request,
        "post_detail.html",
        {"post":post},
    )
# def post_add(request):    
#     if request.method == "GET":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#         return render(request, "post_add.html", {"form": form},)
#     else:
#         post = Post(title=request.POST['title'], text=request.POST['text'])
#         post.save()
#         return HttpResponseRedirect("/")

# Sir ko code
@login_required
def post_add(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) 
            post.author = request.user
            post.save()
        return HttpResponseRedirect("/")
    else:
        form = PostForm()
        return render(request,"post_add.html",{"form": form},
        )

# Ishan's code
# def post_add(request):
#     form = PostForm()
#     if request.method == "POST":
#         post = Post.objects.create(
#             title = request.POST.get('title'),
#             text = request.POST.get('text'),
#             author = request.user
#         )
#         return HttpResponseRedirect("/")
#     else:
#         return render (request, "post_add.html", {"form": form})

@login_required
def draft_list(request):
    #drafts = Post.objects.all()
    drafts = Post.objects.filter(published_date__isnull= True).order_by('-created_date')
    return render(
    request,
    "draft_list.html",
    {"drafts": drafts},
    )
@login_required
def draft_detail(request, pk):
    #post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post,pk=pk)
    return render (
        request,
        "draft_detail.html",
        {"post":post},
    )
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.published_date = timezone.now()
    post.save()
    return HttpResponseRedirect("/")
    
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return HttpResponseRedirect("/")


#This edit works too. This is the main code for the edit.
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save (commit= False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect("/draft-list/")
    else:
        form = PostForm(instance=post)
        return render(request,"post_edit.html", {"form" : form, "post": post})

#Yo muni ko code le edit garcha ra uta template ma '.' haliyeko cha.
# Tyo dot le required logic tancha. 
 
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save (commit= False)
#             post.author = request.user
#             post.save()
#             return HttpResponseRedirect("/")
#     else:
#         form = PostForm(instance=post)
#         return render(request,"post_edit.html", {"form" : form})