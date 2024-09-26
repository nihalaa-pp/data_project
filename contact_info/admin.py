from django.contrib import admin
from .models import Contact

# Check if ContactPerson is already registered

admin.site.register(Contact)