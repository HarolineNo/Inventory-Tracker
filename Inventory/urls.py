from django.urls import path
from .views import InventoryView, MenuView, RecipeView, PurchaseView

urlpatterns = [
    path('ingredients/', InventoryView.as_view(), name='ingredients_list'),
    path('menu/', MenuView.as_view(), name='menu_items'),
    path('recipes/', RecipeView.as_view(), name='recipe_requirements'),
    path('purchases/', PurchaseView.as_view(), name='purchase_log')
]