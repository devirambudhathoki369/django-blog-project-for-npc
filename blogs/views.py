from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog, Category
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect


def post_by_category(request, category_id):
    posts = Blog.objects.filter(category=category_id, status=1)
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'posts_by_category.html', context)