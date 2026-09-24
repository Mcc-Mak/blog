"""URL routing for the personal_web application."""
from django.urls import path
from . import views
# --- Page routes ---
urlpatterns = [
    path('home', views.index),
    path('resume', views.resume),
    path('blog', views.blog),
    path('gallery', views.gallery),
    path('blog_add', views.add),
    path('blog_delete', views.delete),
]
# --- Serve uploaded media files in debug mode ---
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)