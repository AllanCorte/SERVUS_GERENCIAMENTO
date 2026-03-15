from django.urls import path
from nucleus.views import nucleus

urlpatterns = [
    path('', nucleus),  # nucleo
]
