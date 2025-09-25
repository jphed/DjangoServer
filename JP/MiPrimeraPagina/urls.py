from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('random/', views.randomize, name='randomize'),
    path('saludo/<str:nombre>/', views.saludo, name='saludo'),
    path('index1/', views.index1, name='index1'),
    path('about/', views.about, name='about'),
    path('sumar/', views.sumar, name='sumar'),
    path('indextest/', views.indextest, name='indextest'),
]