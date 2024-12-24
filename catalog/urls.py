from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    CategoryDetailView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='catalog_list'),
    path('list_category/', CategoryListView.as_view(), name='list_category'),
    path('detail_category/<int:pk>/', CategoryDetailView.as_view(), name='detail_category'),
    path('product/new_product/', ProductCreateView.as_view(), name='create_product'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='products_detail'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
]
