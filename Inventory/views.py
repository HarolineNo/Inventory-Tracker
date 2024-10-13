from django.shortcuts import render, redirect
from django.views.generic import ListView
from Inventory.models import*
from django.db.models import Sum, F, FloatField
from .models import Ingredient
from django.contrib import messages
from .forms import*

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

class DashboardView(ListView):
    model = Dashboard
    template_name = 'inventory/dashboard.html'
    context_object_name = 'dashboard'

def add_ingredient(request):
    if request.method == "POST":
        ingredient = Ingredient(
            name=request.POST['name'],
            quantity=request.POST['quantity'],
            unit=request.POST['unit'],
            unit_price=request.POST['unit_price']
        )
        ingredient.save()  
        return redirect('ingredients_list')
    return render(request, 'ingredients_list')

def add_item(request):
    if request.method == "POST":
        menu = MenuItem(
            item=request.POST['item'],
            price=request.POST['price'],
        )
        menu.save()  
        return redirect('menu_items')
    return render(request, 'menu_items')

def add_recipe(request):
    if request.method == "POST":
        recipe = RecipeRequirement(
            item=request.POST['item'],
            ingredient=request.POST['ingredient'],
            quantity=request.POST['quantity'],
            unit=request.POST['unit'],
            ingredient_price=request.POST['ingredient_price']
        )
        recipe.save()
        return redirect('recipe_requirements')
    return render(request, 'forms/inventory/recipeform.html')

def add_purchase(request):
    if request.method == "POST":
        purchase = Purchase(
            item=request.POST['item'],
            cost=request.POST['cost'],
        )
        purchase.save()  
        return redirect('purchase_log')
    return render(request, 'purchase_log')
    

def menuform_view(request):
    return render(request, 'forms/inventory/menuform.html')

def recipeform_view(request):
    return render(request, 'forms/inventory/recipeform.html')

def purform_view(request):
    return render(request, 'forms/inventory/purform.html')

def delete_item(request, id):
     obj = Ingredient.objects.get(id=id)
     obj.delete()
     return redirect('ingredients_list')

def delete_menu(request, id):
     obj = MenuItem.objects.get(id=id)
     obj.delete()
     return redirect('menu_items')

def delete_recipe(request, id):
     obj = RecipeRequirement.objects.get(id=id)
     obj.delete()
     return redirect('recipe_requirements')

def delete_purchase(request, id):
     obj = Purchase.objects.get(id=id)
     obj.delete()
     return redirect('purchase_log')

def edit_menu(request, id):
     obj = MenuItem.objects.get(id=id)
     menudict = {
          'item' : obj.item,
          'price' : obj.price,
          'id' : id
     }
     return render(request,'forms/inventory/edit_menu_form.html', context=menudict)

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

def update_menu(request, id):
     if request.method == "POST":
        obj = MenuItem.objects.get(id=id)
        obj.item = request.POST['item']
        obj.price = request.POST['price']
        obj.save()
        return redirect('menu_items')
     return render(request, 'menu_items')

def edit_recipe(request, id):
     obj = RecipeRequirement.objects.get(id=id)
     recipedict = {
          'item' : obj.item,
          'ingredient' : obj.ingredient,
          'quantity' : obj.quantity,
          'unit' : obj.unit,
          'ingredient_price' : obj.ingredient_price,
          'id' : id
     }
     return render(request,'forms/inventory/edit_recipe_form.html', context=recipedict)

def update_recipe(request, id):
     obj = RecipeRequirement.objects.get(id=id)
     obj.item = request.POST['item']
     obj.ingredient = request.POST['ingredient']
     obj.quantity = request.POST['quantity']
     obj.unit = request.POST['unit']
     obj.ingredient_price = request.POST['ingredient_price']
     obj.save()
     return redirect('recipe_requirements')

def make_purchase(request, id, quantity):
    ingredient = Ingredient.objects.get(id=id)

    if ingredient.quantity >= quantity:
        ingredient.quantity -= quantity
        ingredient.save()
        Purchase.objects.create(ingredient=ingredient, quantity=quantity)
        messages.success(request, f'Purchase successful: {quantity} {ingredient.unit} of {ingredient.name} purchased.')
    else:
        messages.error(request, f'Insufficient stock for {ingredient.name}. {ingredient.quantity}{ingredient.unit} available.')
    return redirect('purchase_log')

def money(request):
    total_cost = sum(ingredient.unit_price * ingredient.quantity for ingredient in Ingredient.objects.all())

    total_revenue = sum(purchase.menu_item.price * purchase.quantity for purchase in Purchase.objects.all())

    profit = total_revenue - total_cost

    total_money = {
        'total_cost': total_cost,
        'total_revenue': total_revenue,
        'profit': profit,
        'ingredients': Ingredient.objects.all(),
    }
    return render(request, 'inventory.html', total_money)
