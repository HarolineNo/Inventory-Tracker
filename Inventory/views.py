from django.shortcuts import render, redirect
from django.views.generic import ListView
from Inventory.models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.db.models import Sum, F, FloatField
from .models import Ingredient

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

def add_ingredient(request):
    if request.method == "POST":
        # Create a new Ingredient instance with the form data
        ingredient = Ingredient(
            name=request.POST['name'],
            quantity=request.POST['quantity'],
            unit=request.POST['unit'],
            unit_price=request.POST['unit_price']
        )
        ingredient.save()  # Save the new ingredient to the database
        return redirect('ingredients_list')

        # Redirect to the ingredients list after saving
    return render(request, 'ingredients_list')
    
def inform_view(request):
    return render(request, 'forms/inventory/inform.html')

def delete_item(request, id):
     obj = Ingredient.objects.get(id=id)
     obj.delete()
     return redirect('ingredients_list')

def edit_item(request, id):
     obj = Ingredient.objects.get(id=id)
     ingredientdict = {
          'name' : obj.name,
          'quantity' : obj.quantity,
          'unit' : obj.unit,
          'unit_price' : obj.unit_price,
          'id' : id
     }
     return render(request,'forms/inventory/edit.html', context=ingredientdict)

def update(request, id):
     obj = Ingredient.objects.get(id=id)
     obj.name = request.POST['name']
     obj.quantity = request.POST['quantity']
     obj.unit = request.POST['unit']
     obj.unit_price = request.POST['unit_price']
     obj.save()
     return redirect('ingredients_list')