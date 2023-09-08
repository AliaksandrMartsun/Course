from django.urls import path
from Shop import views

urlpatterns = [
    path('', views.index, name="index"),
]