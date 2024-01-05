from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='homepage'),
    path('album/<slug:album_slug>/', views.HomeView.as_view(), name='album_wise_musician'),
    path('director/', include('director.urls')),
    path('musician/', include('musicians.urls')),
    path('albums/', include('albums.urls')),
]
