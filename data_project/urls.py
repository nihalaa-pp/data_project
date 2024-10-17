"""
URL configuration for data_project project.

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
from django.urls import path, include
from django.views.generic import RedirectView
from business_info import views
from contact_info.views import login_view

urlpatterns = [

    path('', RedirectView.as_view(url='/contacts/', permanent=False)),  # Redirect root to contacts
    path('admin/', admin.site.urls),
    path('business/', include('business_info.urls', namespace='business_info')),
    path('contacts/', include('contact_info.urls', namespace='contact_info')),  
    path('success/', views.success_page, name='success_page'),# Keep this line
    path('login/', login_view, name='login'),
     path('', RedirectView.as_view(url='/contacts/', permanent=False)),  
    path('admin/', admin.site.urls),
    path('business/', include('business_info.urls', namespace='business_info')),
    path('contacts/', include('contact_info.urls', namespace='contact_info')),  
    path('success/', views.success_page, name='success_page'),
    path('login/', login_view, name='login'),
    ]

