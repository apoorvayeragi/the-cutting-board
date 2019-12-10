from django.contrib import admin
from .models import Recipe, Ingredients

# Register your models here.
#admin.site.register(Recipe)
#admin.site.register(Ingredients)


class IngredientsInline(admin.TabularInline):
    model = Ingredients
    extra = 3


class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['recipe_name']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Procedure', {'fields': ['recipe_procedure']}),
    ]
    inlines = [IngredientsInline]

    list_display = ('recipe_name', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']


admin.site.register(Recipe, RecipeAdmin)


