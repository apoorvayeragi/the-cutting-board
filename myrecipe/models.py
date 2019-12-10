from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50)
    recipe_procedure = models.TextField()
    pub_date = models.DateTimeField('date published')
    #ingredient = models.ManyToManyField(Ingredients)

    def __str__(self):
        return self.recipe_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=50)
    units = [
        ("pound", "pound"),
        ("whole", "whole"),
        ("tea spoon", "tea spoon"),
        ("table spoon", "table spoon"),
        ("liter", "liter"),
        ("cup", "cup"),
    ]
    measurement_choice = models.CharField(
        max_length=20,
        choices=units,
        default='whole'
    )
    ingredient_quantity = models.IntegerField()

