from django.contrib import admin
from .models import NewsCategory, NewsArticle

# Register your models here.

admin.site.register(NewsCategory)
admin.site.register(NewsArticle)