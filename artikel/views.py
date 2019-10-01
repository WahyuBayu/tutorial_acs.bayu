from django.shortcuts import render
from django.views.generic import ListView, DetailView

# load model

from .models import Artikel

# Create your views here.

class ArtikelKategoriListView(ListView):
    model = Artikel
    template_name = "artikel/artikel_kategori_list.html"
    context_object_name = 'artikel_list'
    ordering = ['-published']
    def get_queryset(self):
        # artikel_per_kategori = self.model.objects.filter(kategori=self.kwargs['kategori'])
        # # return super().get_queryset()
        # print(artikel_per_kategori)
        print(self.kwargs)


class ArtikelListView(ListView):
    model = Artikel
    template_name = "artikel/artikel_list.html"
    context_object_name = 'artikel_list'
    ordering = ['-published']
    paginate_by = 3

    def get_context_data(self, *args,**kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct
        self.kwargs.update({'kategori_list':kategori_list})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)

class ArtikelDetailView(DetailView):
    model = Artikel
    template_name = "artikel/artikel_detail.html"
    context_object_name = 'artikel'