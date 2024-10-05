from django.urls import path
from .views import InventoryView, MenuView, RecipeView, PurchaseView, add_ingredient, inform_view, delete_item, edit_item, update

urlpatterns = [
    path('ingredients/', InventoryView.as_view(), name='ingredients_list'),
    path('menu/', MenuView.as_view(), name='menu_items'),
    path('recipes/', RecipeView.as_view(), name='recipe_requirements'),
    path('purchases/', PurchaseView.as_view(), name='purchase_log'),
    path('add_ingredients/', add_ingredient, name='add_ingredients'),
    path('inform/', inform_view, name='inform_view'),
    path('delete-ingredient/<int:id>', delete_item, name='delete_item'),
    path('edit-item/<int:id>/', edit_item, name='edit_item'),
    path('update/<int:id>/', update, name='update')
]