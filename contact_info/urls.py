
from django.urls import path
from . import views  # Import views here
from .views import login_view,logout_view

# contacts/urls.py
from django.urls import path
from . import views


app_name = 'contacts'

urlpatterns = [
    path('', views.login_view, name='login'),  # Redirects the root to the login view
    path('login/', views.login_view, name='login'),  # Login URL
    path('logout/', views.logout_view, name='logout'),  # Logout URL
    path('landing_page/', views.landing_page, name='landing_page'),  # Landing page
    path('add_contact/', views.add_contact, name='add_contact'),  # Other URLs...
    path('contact_list/', views.contact_list, name='contact_list'),
    path('edit_contact/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('delete_contact/<int:pk>/', views.delete_contact, name='delete_contact'),
]
