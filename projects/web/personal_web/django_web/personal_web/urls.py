from django.urls import path
from . import views






urlpatterns = [
    path('home',views.index),
    path('resume',views.resume),
    path('blog',views.blog),
    path('gallery',views.gallery),
    path('blog_add',views.add),
    path('blog_delete',views.delete),
    
    
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    