from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy

@method_decorator(login_required, name='dispatch')
class AddCreateAlbumView(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('add_album')
    def form_valid(self, form):
        form.instance.director = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class EditAlbumView(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'edit_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

