from django.contrib import admin
from .models import Article as ArticleModel


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'status')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'descriptions')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', '-publish']


admin.site.register(ArticleModel, ArticleAdmin)
