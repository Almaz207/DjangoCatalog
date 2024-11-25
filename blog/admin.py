from django.contrib import admin
from blog.models import Record



@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ("id", "heading", "number_of_views", "date_of_creation", "sign_of_publication",)
    list_filter = ("sign_of_publication",)
    search_fields = ("heading", "sign_of_publication",)
