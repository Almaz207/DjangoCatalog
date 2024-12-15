from django.db import models
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', help_text='Введите название категории')
    description = models.TextField(null=True, blank=True, verbose_name='Описание категории')

    def __str__(self):
        return f'{self.name} '

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(verbose_name='Название продукта')
    description = models.TextField(null=True, blank=True, verbose_name='Описание продукта')
    image = models.ImageField(upload_to='catalog/photo', null=True, blank=True, verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.FloatField(verbose_name='Цена', help_text='Укажите цену продукта')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False, verbose_name='Опубликован')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} '

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['category', 'name']
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]
