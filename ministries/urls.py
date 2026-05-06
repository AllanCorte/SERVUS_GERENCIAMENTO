from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ministerios, name='lista_ministerios'),
    path('<int:pk>/', views.detalhe_ministerio, name='detalhe_ministerio'),
    path('novo/', views.novo_ministerio, name='novo_ministerio'),
    path('<int:pk>/editar/', views.editar_ministerio,
         name='editar_ministerio'),
    path('<int:pk>/deletar/', views.deletar_ministerio,
         name='deletar_ministerio'),
]
