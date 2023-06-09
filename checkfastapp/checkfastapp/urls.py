"""checkfastapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from accounts.views import register, RegisterView, ProfileView,login
from .views import home, about_us, pricing,demo


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),  
    path("pricing/", pricing, name="pricing"),
    path("about_us/", about_us, name="about_us"),
    path("demo/", demo, name="demo"),
    path("login/", login, name="login"),  
    #path("dashboard", views.dashboard, name="dashboard"),  
    path("register/", RegisterView.as_view(), name="register"),
    path('dashboard/', include('accounts.urls'),name='dashboard'),
    # path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),  

]
