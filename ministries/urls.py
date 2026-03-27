from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ministerios, name='lista_ministerios'),
    path('<int:pk>/', views.detalhe_ministerio, name='detalhe_ministerio'),
    path('novo/', views.novo_ministerio, name='novo_mministerio'),
]
