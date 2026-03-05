from django.urls import path
from nucleus.views import nucleus

urlpatterns = [
    path('nucleo/', nucleus),  # nucleo
]
