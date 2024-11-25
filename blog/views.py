from django.shortcuts import render
from blog.models import Record
from django.urls import reverse_lazy, reverse

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


class RecordCreateView(CreateView):
    model = Record
    fields = ['heading', 'content', 'preview', 'sign_of_publication']
    template_name = 'blog/record_form.html'
    success_url = reverse_lazy('blog:record_list')


class RecordListView(ListView):
    model = Record
    template_name = 'blog/record_list.html'
    context_object_name = 'record_list'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(sign_of_publication=True)
        return queryset


class RecordDetailView(DetailView):
    model = Record
    template_name = 'blog/record_detail.html'
    context_object_name = 'record'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class RecordUpdateView(UpdateView):
    model = Record
    fields = ['heading', 'content', 'preview', 'sign_of_publication']
    template_name = 'blog/record_form.html'
    success_url = reverse_lazy('blog:record_list')

    def get_success_url(self):
        return reverse('blog:record_detail', args=[self.kwargs.get('pk')])


class RecordDeleteView(DeleteView):
    model = Record
    template_name = 'blog/record_confirm_delete.html'
    success_url = reverse_lazy('blog:record_list')
