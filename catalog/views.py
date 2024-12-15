from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden, request
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy('catalog:catalog_list')

    def form_valid(self, form):
        form.object.owner = self.request.user
        return form.object.owner


class ProductListView(ListView):
    model = Product
    form_class = ProductForm


class ProductDetailView(DetailView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_detail.html"


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy('catalog:catalog_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.change_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy('catalog:catalog_list')
    permission_required = 'catalog.delete_product'
