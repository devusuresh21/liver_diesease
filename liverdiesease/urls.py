from django.urls import path
from django.urls import include, path

from . import views

urlpatterns = [
    path('predict/', views.predict, name='predict'),
    
]
