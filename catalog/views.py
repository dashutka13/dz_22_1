from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product, Blog


class PokemonListView(ListView):
    model = Product


def home_page(request):
    return render(request, 'catalog/home_page.html')


class PokemonDetailView(DetailView):
    model = Product


class BlogListView(ListView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('blog_title', 'preview', 'body')
    success_url = reverse_lazy('catalog:blog')


class BlogDetailView(DetailView):
    model = Blog


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('blog_title', 'preview', 'body')
    success_url = reverse_lazy('catalog:blog')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog')

