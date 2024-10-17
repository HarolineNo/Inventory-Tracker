from django import forms
from .models import Ingredient
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit', 'unit_price']

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
