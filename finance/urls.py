from django.urls import path
from finance.views import finance

urlpatterns = [
    path('', finance),  # home
]
