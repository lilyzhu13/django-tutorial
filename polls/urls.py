from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^details/(?P<question_id>[0-9]+)/$', views.details, name='details'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
]
