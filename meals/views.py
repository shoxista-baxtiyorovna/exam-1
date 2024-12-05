from django.shortcuts import render
from .models import Meal

def meal_list(request):
    meal_name = request.GET.get('mealName')
    ingredients = request.GET.get('ingredients')
    price = request.GET.get('price')
    type = request.GET.get('type')
    cuisine = request.GET.get('cuisine')
    if (meal_name is not None
            and ingredients is not None
            and price is not None
            and type is not None
            and cuisine is not None):
        Meal.objects.create(
            meal_name=meal_name,
            ingredients=ingredients,
            price=price,
            type=type,
            cuisine=cuisine
        )
    meals = Meal.objects.all()
    ctx = {'meals': meals}
    return render(request, 'meals/meal_list.html', ctx)

