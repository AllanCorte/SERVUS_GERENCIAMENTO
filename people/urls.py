from django.urls import path
from people.views import people

urlpatterns = [
    path('pessoas/', people),  # pessoa
]
