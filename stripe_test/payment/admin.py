from django.contrib import admin
from .models import Item


# Register your models here.
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name', )
    search_fields = ('name', 'description')
    list_filter = ('name', 'price',)  # фильтрация



admin.site.register(Item, ItemsAdmin)