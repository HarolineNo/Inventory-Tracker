from django.shortcuts import render
from django.views.generic import ListView
from Inventory.models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.db.models import Sum, F, FloatField

# Create your views here.

class InventoryView(ListView):
    model = Ingredient
    template_name = 'inventory/inventory.html'
    context_object_name = 'ingredients'

class MenuView(ListView):
    model = MenuItem
    template_name = 'inventory/menu.html'
    context_object_name = 'menu'

class RecipeView(ListView):
    model = RecipeRequirement
    template_name = 'inventory/recipe.html'
    context_object_name = 'recipe'

class PurchaseView(ListView):
    model = Purchase
    template_name = 'inventory/purchase.html'
    context_object_name = 'purchases'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            
            revenue = Purchase.objects.aggregate(total=Sum('cost'))
            cost = RecipeRequirement.objects.aggregate(total=Sum(F('quantity') * F('ingredient_price'), output_field=FloatField()))
            
            context["revenue"] = revenue
            context["cost"] = cost

            return context
    
    

