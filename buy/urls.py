from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^gold/(?P<num>[0-9]+)/$', views.buyGold, name='buyGold'),
]