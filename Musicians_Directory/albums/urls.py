from django.urls import path
from . import views

urlpatterns = [
    path('add_album/', views.AddCreateAlbumView.as_view(), name='add_album'),
    path('edit_album/<int:id>/', views.EditAlbumView.as_view(), name='edit_album'),
]