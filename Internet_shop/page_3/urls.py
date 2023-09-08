from django.urls import path
from page_3 import views



urlpatterns = [
    path('create-flower/', views.create_flower, name='create_flower'),
    path('create-client/', views.create_client, name='create_client'),
    path('get_flower/', views.get_flower, name='get_flower'),
]