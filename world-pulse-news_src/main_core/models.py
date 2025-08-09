from django.db import models
from django.utils.text import slugify
# Create your models here.

class NewsCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = base_slug
            num = 1

            while NewsCategory.objects.filter(slug=unique_slug).exclude(pk=self.pk).exists():
                unique_slug = f"{base_slug}-{num}"
                num += 1

            self.slug = unique_slug

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'News Category'
        verbose_name_plural = 'News Categories'

    def __str__(self):
        return self.name
    

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    images = models.ImageField(upload_to='news_images/', blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            num = 1

            while NewsArticle.objects.filter(slug=unique_slug).exclude(pk=self.pk).exists():
                unique_slug = f"{base_slug}-{num}"
                num += 1

            self.slug = unique_slug

        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'News Article'
        verbose_name_plural = 'News Articles'
        ordering = ['-published_date']

    def __str__(self):
        return self.title
    


class Event(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  # يحفظ وقت الإنشاء
    updated_at = models.DateTimeField(auto_now=True)      # يحفظ وقت آخر تعديل

    def __str__(self):
        return self.title
