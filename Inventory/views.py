from django.shortcuts import render, redirect
from django.views.generic import ListView
from Inventory.models import*
from django.db.models import Count
from .models import Ingredient
from django.contrib import messages
from .forms import*
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models.functions import TruncDate
from .models import Action


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = MenuItem.objects.all()
        context['ingredients'] = Ingredient.objects.all()  
        return context

class PurchaseView(ListView):
    model = Purchase
    template_name = 'inventory/purchase.html'
    context_object_name = 'purchases'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = RecipeRequirement.objects.all() 
        return context

class DashboardView(ListView):
    model = Dashboard
    template_name = 'inventory/dashboard.html'
    context_object_name = 'dashboard'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_cost = 0 
        total_revenue = 0

        purchases = Purchase.objects.all()

        for purchase in purchases: 
            total_cost += purchase.unit_price * purchase.quantity 

        for purchase in purchases:
            total_revenue += purchase.cost  

        profit = total_revenue - total_cost

        profit_percent = 100 * (profit/(total_revenue + total_cost + profit))
        cost_percent = 100 * (total_cost/(total_revenue + total_cost + profit))
        revenue_percent = 100 * (total_revenue/(total_revenue + total_cost + profit))

        daily_purchases = (Purchase.objects.annotate(date=TruncDate('timestamp')).values('date').annotate(count=Count('id')).order_by('date')
        )
        
        purchase_date = [sale['date'] for sale in daily_purchases]
        purchase_num = [sale['count'] for sale in daily_purchases]

        recent_actions = Action.objects.order_by('-timestamp')[:10]
        
        context['recent_actions'] = recent_actions
        context['purchase_count'] = purchases.count()
        context['total_cost'] = total_cost
        context['total_revenue'] = total_revenue
        context['profit'] = profit
        context['profit_percent'] = profit_percent
        context['revenue_percent'] = revenue_percent
        context['cost_percent'] = cost_percent
        context['purchase_date'] = purchase_date
        context['purchase_num'] = purchase_num
        return context


def add_ingredient(request):
    if request.method == "POST":
        ingredient = Ingredient(
            category=request.POST.get('category', False),
            name=request.POST['name'],
            quantity=request.POST['quantity'],
            unit=request.POST['unit'],
            unit_price=request.POST['unit_price'],
            date_purchased=request.POST.get('date_purchased'),
            expiration_date=request.POST.get('expiration_date')
        )
        ingredient.save()  
        Action.objects.create(
            user=request.user,
            action_type='added',
            item=ingredient.name
        )
        return redirect('ingredients_list')
    return render(request, 'ingredients_list')

def add_item(request):
    if request.method == "POST":
        menu = MenuItem(
            item=request.POST['item'],
            price=request.POST['price']
        )
        menu.save()  
        Action.objects.create(
            user=request.user,
            action_type='added',
            item=menu.item
        )
        return redirect('menu_items')
    return render(request, 'menu_items')

def add_recipe(request):
    if request.method == "POST":
        ingredient_id = request.POST.get('ingredient')  
        menu_id = request.POST.get('item') 

        ingredient_name = Ingredient.objects.get(id=ingredient_id)
        menu_item = MenuItem.objects.get(id=menu_id)
        menu_price = request.POST.get('price')

        recipe = RecipeRequirement(
            item=menu_item,
            ingredient=ingredient_name,
            quantity=request.POST['quantity'],
            unit=request.POST['unit'],
            ingredient_price=request.POST['ingredient_price'],
            price=menu_price
        )
        recipe.save()
        Action.objects.create(
            user=request.user,
            action_type='added',
            item=recipe.item
        )
        return redirect('recipe_requirements')
    return render(request, 'forms/inventory/recipeform.html')

def add_purchase(request):
    if request.method == "POST":
        recipe_item_id = request.POST.get('item')  
        
        recipe = RecipeRequirement.objects.get(id=recipe_item_id)
        
        ingredient = recipe.ingredient
        
        if ingredient.quantity < recipe.quantity:
            return redirect('purchase_log')
        
        ingredient.quantity -= recipe.quantity
        ingredient.save()

        purchase = Purchase(
            item=recipe.item, 
            ingredient=recipe.ingredient,  
            quantity=recipe.quantity,  
            unit_price=recipe.ingredient_price,  
            cost=recipe.price
        )
        purchase.save()  
        Action.objects.create(
            user=request.user,
            action_type='added',
            item=purchase.item
        )
        return redirect('purchase_log')
    return render(request, 'purchase_log')
    

def delete_item(request, id):
     obj = Ingredient.objects.get(id=id)
     Action.objects.create(
            user=request.user,
            action_type='deleted',
            item=obj.name
        )
     obj.delete()
     return redirect('ingredients_list')

def delete_menu(request, id):
     obj = MenuItem.objects.get(id=id)
     Action.objects.create(
            user=request.user,
            action_type='deleted',
            item=obj.item
        )
     obj.delete()
     return redirect('menu_items')

def delete_recipe(request, id):
     obj = RecipeRequirement.objects.get(id=id)
     Action.objects.create(
            user=request.user,
            action_type='deleted',
            item=obj.item
        )
     obj.delete()
     return redirect('recipe_requirements')

def delete_purchase(request, id):
     obj = Purchase.objects.get(id=id)
     Action.objects.create(
            user=request.user,
            action_type='deleted',
            item=obj.item
        )
     obj.delete()
     return redirect('purchase_log')

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

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login')

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')  

        user = User.objects.create_user(username=username, password=password)
        login(request, user)  
        messages.success(request, "Signup successful!")
        return redirect('dashboard') 

    return render(request, 'signup')