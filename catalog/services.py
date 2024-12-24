from config.settings import CACHE_ENABLED
from django.core.cache import cache
from catalog.models import Category, Product


def get_list_product_in_category(category_id):
    if not CACHE_ENABLED:
        category = Category.objects.get(id=category_id)
        return Product.objects.filter(category=category.id)
    key = f'list_product_{category_id}'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.filter(category=Category.objects.get(id=category_id))
    cache.set(key, products, 60)
    return products
