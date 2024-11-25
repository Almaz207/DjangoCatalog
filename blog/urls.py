from django.urls import path
from blog.apps import BlogConfig
from blog.views import RecordCreateView, RecordListView, RecordDetailView, RecordUpdateView, RecordDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', RecordListView.as_view(), name='record_list'),
    path('new_record/', RecordCreateView.as_view(), name='new_record'),
    path('record/<int:pk>/', RecordDetailView.as_view(), name='record_detail'),
    path('record/<int:pk>/update', RecordUpdateView.as_view(), name='record_update'),
    path('record/<int:pk>/delete', RecordDeleteView.as_view(), name='record_delete'),
]
