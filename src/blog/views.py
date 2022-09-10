from django.shortcuts import get_object_or_404, render

from blog.models import Article


def home(request):
    articles = Article.objects.filter(status='p').order_by('-publish')
    template = 'blog/home.html'
    context = {
        "articles": articles
    }
    return render(request, template, context)


def detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    template = 'blog/detail.html'
    context = {
        "article": article
    }
    return render(request, template, context)
