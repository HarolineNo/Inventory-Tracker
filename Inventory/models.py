from django.db import models

# Create your models here.

class Ingredient(models.Model):
    category = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_purchased = models.DateField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    item = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item

class RecipeRequirement(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=0)
    unit = models.CharField(max_length=50, default='units')
    ingredient_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.item} requires {self.quantity} of {self.ingredient}"

class Purchase(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.item} was purchased on {self.timestamp}"
    
class Dashboard(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    