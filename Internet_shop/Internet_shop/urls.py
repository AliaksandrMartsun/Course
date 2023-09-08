"""
URL configuration for Internet_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Shop/', include('Shop.urls')),
    path('page_1/', include('page_1.urls')),
    path('page_2/', include('page_2.urls')),
    path('page_3/', include('page_3.urls')),
    path('page_4/', include('page_4.urls')),
    path('page_5/', include('page_5.urls')),
    path('page_6/', include('page_6.urls')),
    path('page_7/', include('page_7.urls')),

]
