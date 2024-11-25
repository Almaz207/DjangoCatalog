from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView
app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='catalog_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='products_detail'),
]
