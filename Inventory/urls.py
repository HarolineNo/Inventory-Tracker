from django.urls import path
from Inventory.views import* 
from .apiViews import*

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('ingredients/', InventoryView.as_view(), name='ingredients_list'),
    path('menu/', MenuView.as_view(), name='menu_items'),
    path('recipes/', RecipeView.as_view(), name='recipe_requirements'),
    path('purchases/', PurchaseView.as_view(), name='purchase_log'),
    path('add_ingredients/', add_ingredient, name='add_ingredients'),
    path('add_item/', add_item, name='add_item'),
    path('add_recipe/', add_recipe, name='add_recipe'),
    path('add_purchase/', add_purchase, name='add_purchase'),
    path('delete-ingredient/<int:id>/', delete_item, name='delete_item'),
    path('delete-menu/<int:id>/', delete_menu, name='delete_menu'),
    path('delete-recipe/<int:id>/', delete_recipe, name='delete_recipe'),
    path('delete-purchase/<int:id>/', delete_purchase, name='delete_purchase'),
    path('purchase/<int:ingredient_id>/<int:quantity>/', make_purchase, name='make_purchase'),
    path('save_inventory', save_inventory, name='save_inventory')
]