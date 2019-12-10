from django.shortcuts import render
from django.http import Http404
from .models import Recipe
# Create your views here.
from django.http import HttpResponse
from django.views import generic

#def index(request):
 #   latest_recipe_list = Recipe.objects.order_by('-pub_date')[:5]
  #  context = {'latest_recipe_list': latest_recipe_list}
   # return render(request, 'myrecipe/index.html', context)


class IndexView(generic.ListView):
    template_name = 'myrecipe/index.html'
    context_object_name = 'latest_recipe_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Recipe.objects.order_by('-pub_date')[:5]


def detail(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    return render(request, 'myrecipe/detail.html', {'recipe': recipe})


def results(request, recipe_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % recipe_id)

