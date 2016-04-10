from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^gold/(?P<num>[0-9]+)/$', views.buyGold, name='buyGold'),
    url(r'^login/$', views.login_game, name='login'),
    url(r'^paycallback/$', views.anysdk_payment, name='pay'),
]