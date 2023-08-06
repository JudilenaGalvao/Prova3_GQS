"""
URL configuration for Apicultura project.

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
from Producao.views import pagina_principal
from Producao.views import login_view

"""urlpatterns = [
    path('admin/', admin.site.urls),
]"""

urlpatterns = [
    path('pagina_principal', pagina_principal, name='pagina_principal'),
    path('admin/', admin.site.urls),
    path('Producao/', include('Producao.urls', namespace='Producao')),
    path('', login_view, name='login'),
]


