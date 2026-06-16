from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
 path('nosotros/', views.nosotros, name='nosotros'),
 path('contacto/', views.contacto, name='contacto'),
 path('musica/', views.musica, name='musica'),
 path('piano/', views.piano, name='piano'),
 path('tec/', views.tec, name='tec'),
 path('juanin/', views.juanin, name='juanin'),
]   