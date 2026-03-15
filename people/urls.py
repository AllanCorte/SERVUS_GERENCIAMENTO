from django.urls import path
from people.views import people

urlpatterns = [
    path('', people),  # pessoa
]
