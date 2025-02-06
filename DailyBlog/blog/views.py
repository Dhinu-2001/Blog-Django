from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm, CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator

#View for home page
def home(request):
    posts = BlogPost.objects.all().order_by('-pub_date')[:6]
    return render(request, 'home.html', {'posts': posts})

#View for registering user
def register(request): 
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

#View for user login
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect if user is already logged in

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


#View for creating post
@login_required(login_url='login')
def create_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = BlogPostForm()
    return render(request, 'post_form.html', {'form': form})

#View for detail of a post
def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

#View for post listing
def post_list(request):
    post_list = BlogPost.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 6)  # Show 6 posts per page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'post_list.html', {'posts': posts})

#View for listing logged in user's post
@login_required(login_url='login')
def user_post_list(request, user_id):
    post_list = BlogPost.objects.filter(author=user_id).order_by('-pub_date')
    paginator = Paginator(post_list, 6)  # Show 6 posts per page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'post_list.html', {'posts': posts, 'type': 'your_posts'})

#View for edit post
@login_required(login_url='login')
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id, author=request.user)
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form, 'post': post})

#View for delete post
@login_required(login_url='login')
def delete_post(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(BlogPost, id=post_id, author=request.user)
        post.delete()
        return redirect('user_post_list', user_id=request.user.id)
    