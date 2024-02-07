from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home_page, PokemonListView, PokemonDetailView, BlogListView, BlogCreateView, BlogUpdateView, \
    BlogDeleteView, BlogDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', home_page, name='home_page'),
    # path('product/<int:pk>/', product, name='product'),
    path('product/<int:pk>/', PokemonDetailView.as_view(), name='view_product'),
    # path('catalog/', catalog, name='catalog')
    path('catalog/', PokemonListView.as_view(), name='catalog'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='view_blog'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='update_blog'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),
]
