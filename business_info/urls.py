# business_info/urls.py
from django.urls import path
from .views import add_business,business_list,edit_business_view,delete_business_view

from . import views# Ensure this is the correct view

app_name = 'business_info'  # Make sure this matches your namespace

urlpatterns = [
    path('business_list/', business_list, name='business_list'),  # Existing pattern
    path('add_business/', add_business, name='add_business'),  
    path('success/', views.success_page, name='success_page'),
    path('edit_business/<int:id>/', edit_business_view, name='edit_business'),
    path('delete_business/<int:id>/', delete_business_view, name='delete_business'),
    
]
