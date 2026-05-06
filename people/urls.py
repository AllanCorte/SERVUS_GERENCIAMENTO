from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pessoas, name='lista_pessoas'),
    path('<int:pk>/', views.perfil_pessoa, name='perfil_pessoa'),
    path('novo/', views.nova_pessoa, name='nova_pessoa'),
    path('<int:pk>/editar/', views.editar_pessoa, name='editar_pessoa'),
    path('<int:pk>/deletar/', views.deletar_pessoa, name='deletar_pessoa'),
]
