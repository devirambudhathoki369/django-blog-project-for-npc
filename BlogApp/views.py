from django.shortcuts import render
from blogs.models import Blog, Category

def home(request):
    featured_posts = Blog.objects.filter(featured_post=True, status=1).order_by('-created_at')[:1]
    breaking_news = Blog.objects.filter(status=1, featured_post=False).order_by('-created_at')[:4]
    posts = Blog.objects.filter(status=1, featured_post=False).order_by('-created_at')
    context = {
        'featured_posts': featured_posts,
        'breaking_news': breaking_news,
        'posts': posts
    }
    return render(request, 'home.html', context)