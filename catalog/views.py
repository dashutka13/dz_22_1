from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.forms import PokemonForm, VersionForm
from catalog.models import Product, Blog, Version


class IndexView(TemplateView):
    template_name = 'catalog/home_page.html'


class PokemonListView(ListView):
    model = Product


class PokemonCreateView(CreateView):
    model = Product
    form_class = PokemonForm
    success_url = reverse_lazy('catalog:catalog')


class PokemonDetailView(DetailView):
    model = Product


class PokemonUpdateView(UpdateView):
    model = Product
    form_class = PokemonForm

    def get_success_url(self):
        return reverse('catalog:update_product', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class PokemonDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:catalog')


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogCreateView(CreateView):
    model = Blog
    fields = ('blog_title', 'preview', 'body', 'date_of_creation')
    success_url = reverse_lazy('catalog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.blog_title)
            new_blog.save()
        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('blog_title', 'preview', 'body')

    # success_url = reverse_lazy('catalog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.blog_title)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:view_blog', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog')


# class VersionCreateView(CreateView):
#     model = Version
#     form_class = VersionForm
#     success_url = reverse_lazy('catalog:create_version')


# def toggle_activity(request, pk):
#     product_item = get_object_or_404(Product, pk=pk)
#     if product_item.is_active:
#         product_item.is_active = False
#     else:
#         product_item.is_active = True
#
#     product_item.save()
#     return redirect(reverse('catalog:catalog'))
