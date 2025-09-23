from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('random/', views.randomize, name='randomize'),
    path('saludo/<str:nombre>/', views.saludo, name='saludo'),
]