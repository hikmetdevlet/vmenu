from django.contrib import admin
from .models import MenuItem, MenuCategory

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('name', 'description')


    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['image'].widget.attrs['accept'] = 'image/*'
        return form


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order')
    prepopulated_fields = {'slug': ('name',)}


# views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import MenuItem, MenuCategory


class MenuListView(ListView):
    model = MenuCategory
    template_name = 'menu/menu_list.html'
    context_object_name = 'categories'


class MenuItemDetailView(DetailView):
    model = MenuItem
    template_name = 'menu/menu_item_detail.html'
    context_object_name = 'item'


class MenuCategoryDetailView(DetailView):
    model = MenuCategory
    template_name = 'menu/menu_category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = self.object.items.filter(is_available=True)
        return context