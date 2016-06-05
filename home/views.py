from django.shortcuts import render
from .models import Post,Tag
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q
from django.core.mail import send_mail


def me(request):
    # send_mail('CONTACT PAGE SEARCHED', 'HELLLO .', 'sarthak221995@gmail.com',['sarthak221995@gmail.com'], fail_silently=False)
    return render(request, 'home/me.html', {})


def ds(request):
    return render(request, 'home/ds.html', {})



def mee(request):
    email = request.POST.get('email')
    message = request.POST.get('message')
    subject = "Contact Notification from "
    body = "EMAIL: "+email+"\nMessage: "+message
    send_mail(subject, message, email,['sarthak221995@gmail.com'], fail_silently=False)
    return render(request, 'home/me.html', {})
    
	


def post_list(request):
    query =  request.GET.get("q")
    posts_seta = Post.objects.all().order_by('-created')
    posts_setb = Post.objects.all().order_by('-created')
    tagi = Tag.objects.all()
    if query:
        posts_seta= posts_seta.filter(Q(title = query)|Q(author = query)|Q(text = query)).distinct()
    

    paginator = Paginator(posts_seta,2)
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'home/index.html', {'posts': posts,'posts_setb': posts_setb,'tagi': tagi})


def post_tagdetail(request,tag_field):
    
    posts = Post.objects.all
    return render(request, 'home/post_tagdetail.html', {'posts': posts, 'tag_field':tag_field})


















def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'home/post_detail.html', {'post': post})
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
            
#     else:
#         form = PostForm()
#     return render(request, 'home/post_detail.html', {'form': form ,'post': post})






# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
            
#     else:
#         form = PostForm()
#     return render(request, 'home/post_detail.html', {'form': form})






# Create your views here.
