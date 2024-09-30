from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Category
from .forms import RecipeForm

def home(request):
    recipes = Recipe.objects.all().order_by('?')[:5]
    return render(request, 'recipes/home.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})