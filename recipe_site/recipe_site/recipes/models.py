from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructions = models.TextField()
    cooking_time = models.PositiveIntegerField(help_text="Time in minutes")
    image = models.ImageField(upload_to='recipe_images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.TextField(blank=True, help_text="List of ingredients")

    def str(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name

class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)