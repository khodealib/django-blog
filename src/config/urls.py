from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from . import settings as project_settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

if project_settings.DEBUG:
    urlpatterns += static(project_settings.MEDIA_URL, document_root=project_settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
