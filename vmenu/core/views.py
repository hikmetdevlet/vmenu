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

