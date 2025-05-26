from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import views as auth_views

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Q

def article_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'news/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'news/article_detail.html', {'article': article})

@login_required
def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'news/article_form.html', {'form': form})


@login_required
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'news/article_form.html', {'form': form})


@login_required
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('article_list')
    else:
        form = UserCreationForm()
    return render(request, 'news/register.html', {'form': form})

def custom_logout_view(request):
    messages.success(request, "✅ Вы успешно вышли из аккаунта.")
    return auth_views.LogoutView.as_view(next_page='article_list')(request)

# Поисковик
def search_articles(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Article.objects.filter(title__icontains=query) | Article.objects.filter(body__icontains=query)
    return render(request, 'news/search_results.html', {'query': query, 'results': results})

# О нас

def about_page(request):
    return render(request, 'news/about.html')

