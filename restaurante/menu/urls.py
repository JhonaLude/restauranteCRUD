from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_platos, name='lista'),
    path('crear/', views.crear_plato, name='crear'),
    path('eliminar/<int:id>/', views.eliminar_plato, name='eliminar'),
    path('editar/<int:id>/', views.editar_plato, name='editar'),
]