from django.urls import path
from . import views




urlpatterns = [
    path('', views.MenuListView.as_view(), name='menu_list'),
    path('menu/item/<int:pk>/', views.MenuItemDetailView.as_view(), name='menu_item_detail'),
    path('menu/category/<slug:slug>/', views.MenuCategoryDetailView.as_view(), name='menu_category_detail'),
]