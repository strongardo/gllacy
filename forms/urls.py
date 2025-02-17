from django.urls import path
from . import views

urlpatterns = [
    path('newsletter/', views.newsletter, name='newsletter'),
    path('feedback/', views.feedback, name='feedback'),
    path('ty/', views.ty, name='ty'),
    path('search/', views.search, name='search'),
]
