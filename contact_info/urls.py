from django.urls import path
from . import views  # Import views here
from .views import login_view,logout_view

app_name = 'contacts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('', views.contact_list, name='contact_list'),
    path('add/', views.add_contact, name='add_contact'),
    path('edit/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('delete/<int:pk>/', views.delete_contact, name='delete_contact'),
    path('logout/', logout_view, name='logout'),
]
