from time import timezone
from django.shortcuts import render
from .models import Post
from django.http import HttpResponseRedirect
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import get_object_or_404

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
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
def post_add(request):    
    if request.method == "GET":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return render(request, "post_add.html", {"form": form},)
    else:
        post = Post(title=request.POST['title'], text=request.POST['text'])
        post.save()
        return HttpResponseRedirect("/")

# def post_add(request):
#     if request.method == "POST":
#         print(request.post)
#         post = post.object.create(
#             title = request.POST["titles"]
#             text = request.POST["contents"]
#         )
#         return HttpResponseRedirect("/")
#     else:
#         return render (request, "post_add.html")

def post_draft_list(request):
    drafts = Post.objects.filter(published_date__isnull= True).order_by('created_date')
    return render(
    request,
    "draft_list.html",
    {"drafts": drafts},
    )

def draft_detail(request, pk):
    #post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post,pk=pk)
    return render (
        request,
        "draft_detail.html",
        {"post":post},
    )