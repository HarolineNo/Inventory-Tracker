from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import*

@csrf_exempt
def edit_inventory(request):
    ingredient = Ingredient.objects.filter(ingredient_id=request.POST.get('name',''))
    ingredient_obj = serializers.serialize('python',ingredient)
    return JsonResponse(ingredient_obj,safe=False)

@csrf_exempt
def save_inventory(request):
    id=request.POST.get('id','')
    type=request.POST.get('type','')
    value=request.POST.get('value','')
    ingredient=Ingredient.objects.get(id=id)
    if type == "name":
        ingredient.name = value
    if type == "quantity":
        ingredient.quantity = value
    if type == "unit":
        ingredient.unit = value
    if type == "unit_price":
        ingredient.unit_price = value
    ingredient.save()
    return JsonResponse({"Success": "Updated"})