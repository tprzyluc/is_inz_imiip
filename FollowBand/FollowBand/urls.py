"""FollowBand URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path, re_path
from . import views
from django.views.generic import TemplateView
from localization.views import localizationView

urlpatterns = [

    path('', TemplateView.as_view(template_name='start.html'), name = 'home'),
    path('home', TemplateView.as_view(template_name='base.html'), name = 'base'),
    path('admin/',admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('current/',views.view_user_id),
    path('localization/',localizationView), 



    # path(r'admin/', admin.site.urls),
    # path(r'accounts/', include('django.contrib.auth.urls')),
    # #path(r'start/', views.mainpage),
    # path(r'logout/', views.start),
  
   #path(r'homepage/', include('homepage.urls'))
]
