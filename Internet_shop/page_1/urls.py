from django.urls import path
from page_1 import views

urlpatterns = [
    path('', views.index, name="index-view"),
    path('article/<int:year>/', views.year_archive),
]