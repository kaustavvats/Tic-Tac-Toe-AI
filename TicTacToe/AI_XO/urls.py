from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^name/', views.enter_name, name='name'),
    url(r'main/', views.lets_play, name='main'),
]
