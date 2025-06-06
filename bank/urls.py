"""
URL configuration for bank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from online import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('welcome/',views.welcome,name='welcome'),
    path('withdraw/',views.withdraw,name='withdraw'),
    path('deposit/',views.deposit,name='deposit'),
    path('loan/',views.loans,name='loan'),
    path('loaninfo/',views.loaninfo,name='loaninfo'),
    path('custloan/',views.custloan,name='custloan'),
    path('mini/',views.mini,name='mini'),
]
