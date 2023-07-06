from django.urls import path
from . import views

urlpatterns = [
    #path('', views.hello ),
    path('', views.inicio ),
    path('about/', views.about),
    path('esta/', views.esta ),
    path('registro/', views.registro),
    path('home/', views.home),
    path('salir/', views.salir),
    path('ha/', views.ha),
    path('api/', views.api),

]