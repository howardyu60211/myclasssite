from django.urls import path
from .views import login, home

urlpatterns = [
    path('login/', login),
    path('index/', home)
]
