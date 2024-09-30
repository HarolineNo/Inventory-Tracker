from django.shortcuts import render
from django.vivews.generic import ListView
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.db.models import Sum

# Create your views here.

class InventoryView(ListView):
    model = Ingredient
    template = 'inventory/templates/inventory.html'
    name = 'Ingredients'

class MenuView(ListView):
    model = MenuItem
    template = 'inventory/templates/menu.html'
    name = 'Menu'

class RecipeView(ListView):
    model = RecipeRequirement
    template = 'inventory/templates/recipe.html'
    name = 'Recipe Requirements'

class PurchaseView(ListView):
    model = Purchase
    template = 'inventory/templates/purchase.html'
    name = 'Purchases'

    def total_revenue(request):
        revenue = Purchase.objects.aggregrate(total=models.Sum('price'))

        return render(request, 'inventory/template/purchase.html')