from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import product, catalog, home_page

app_name = CatalogConfig.name

urlpatterns = [
    path('', home_page, name='home_page'),
    path('product/<int:pk>/', product, name='product'),
    path('catalog/', catalog, name='catalog')
]
