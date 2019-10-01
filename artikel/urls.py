
from django.conf.urls import url


from .views import (
    ArtikelListView,
    ArtikelDetailView,
    ArtikelKategoriListView,
    )

urlpatterns=[
    url(r'^kategori/(?P<kategori>[\w]+)$', ArtikelKategoriListView.as_view(), name='category'),
    url(r'^detail/(?P<slug>[\w-]+)$', ArtikelDetailView.as_view(), name='detail'),
    url(r'^(?P<page>\d+)$', ArtikelListView.as_view(), name='list'),
]