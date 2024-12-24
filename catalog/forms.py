from django.core.exceptions import ValidationError
from django.forms import ModelForm
from config.settings import bad_words

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].help_text = None
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название',
        })

        self.fields['description'].help_text = None
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание',
        })

        self.fields['image'].help_text = None
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Можете добавить фото',
        })

        self.fields['category'].help_text = None
        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Укажите категорию',
        })

        self.fields['price'].help_text = None
        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'укажите цену продукта',
        })

        self.fields['is_active'].help_text = None
        self.fields['is_active'].widget.attrs.update({
            'placeholder': 'Товар опубликован',
        })



    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError("Цена не может быть равна 0, а темболее не может быть отрицательной ")
        return price

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        for word in bad_words:
            if word in name.lower() or word in description.lower():
                self.add_error('name', f"Слово находится в списке запрещённых слов{bad_words}")


class ProductModeratorForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'is_active')
