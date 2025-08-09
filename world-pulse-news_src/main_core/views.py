from django.shortcuts import render
from .models import NewsArticle, Event, NewsCategory
from django.utils.text import slugify

# Create your views here.


def home(request):
    myNewsCategory = NewsCategory.objects.all()
    news_articles = NewsArticle.objects.all().order_by('-published_date')[:5]
    context = {
        'news_articles': news_articles,
        'myNewsCategory': myNewsCategory,
    }
    return render(request, 'homepage/index.html', context)


def newsgategory(request, slug):
    myNewsCategory = NewsCategory.objects.all()
    news_articles = NewsArticle.objects.filter(category__in=NewsCategory.objects.filter(slug=slug)).order_by('-published_date')
    context = {
        'news_articles': news_articles,
        'myNewsCategory': myNewsCategory,
    }
    return render(request, 'homepage/category.html', context)


def news_detail(request, slug):
    myNewsCategory = NewsCategory.objects.all()
    news_articles = NewsArticle.objects.get(slug=slug)
    context = {
        'news_articles': news_articles,
        'myNewsCategory': myNewsCategory,
    }
    return render(request, 'news/news_detail.html', context)