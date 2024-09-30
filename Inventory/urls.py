from django.urls import path
from .views import InventoryView, MenuView, RecipeView, PurchaseView

urlpatterns = [
    path('ingredients/', InventoryView.as_view()),
    path('menu/', MenuView.as_view()),
    path('recipes/', RecipeView.as_view()),
    path('purchases/', PurchaseView.as_view())
]