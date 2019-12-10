from django.conf.urls import url
from . import views

app_name='myrecipe'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^specifics/(?P<recipe_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<recipe_id>[0-9]+)/results/$', views.results, name='results'),
]

