from django.urls import path
from ministries.views import ministries

urlpatterns = [
    path('', ministries),  # home
]
