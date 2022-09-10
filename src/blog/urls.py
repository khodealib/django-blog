from django.urls import path

from blog.views import *

app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    path('articles/<str:slug>/', detail, name="detail")
]
