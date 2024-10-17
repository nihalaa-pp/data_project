from django.shortcuts import render, redirect, get_object_or_404
from .models import Business, ContactPerson
from .forms import BusinessForm
from django.db.models import Q  # Import Q for complex queries

def add_business(request):
    if request.method == 'POST':
        business_data = {
            'country': request.POST.get('country'),
            'state': request.POST.get('state'),
            'town': request.POST.get('town'),
            
            'name_of_firm': request.POST.get('name_of_firm'),
            'location': request.POST.get('location'),
            'landmark': request.POST.get('landmark'),
            'website_url': request.POST.get('website_url', ''),
            'level': request.POST.get('level'),
            'type': request.POST.get('type'),
            'category': request.POST.get('category'),
        }
        business = Business.objects.create(**business_data)

        contact_person_data = {
            'business': business,
            'name': request.POST.get('contact_person'),
            'designation': request.POST.get('designation'),
            'native_town': request.POST.get('native_town'),
            'mobile_number': request.POST.get('mobile_number', ''),
            'whatsapp_number': request.POST.get('whatsapp_number'),
            'email': request.POST.get('email'),
            'remarks': request.POST.get('remarks'),
        }
        ContactPerson.objects.create(**contact_person_data)

        return redirect('business_info:business_list')
    else:
        return render(request, 'business_info/add_business.html')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Business, ContactPerson
from django.db.models import Q

from django.shortcuts import render, redirect, get_object_or_404
from .models import Business, ContactPerson
from django.db.models import Q

def business_list(request):
    query = request.GET.get('q', '')  # Search query
    filter_country = request.GET.get('country', '')  # Filter for country
    filter_state = request.GET.get('state', '')  # Filter for state
    filter_town = request.GET.get('town', '')  # Filter for town
    filter_type = request.GET.get('type', '')  # Filter for type
    filter_level = request.GET.get('level', '')  # Filter for level
    filter_category = request.GET.get('category', '')  # Filter for category

    # Fetch businesses with filters
    businesses = Business.objects.all()

    # Apply search query
    if query:
        businesses = businesses.filter(name_of_firm__icontains=query)

    # Apply filters
    if filter_country:
        businesses = businesses.filter(country=filter_country)
    
    if filter_state:
        businesses = businesses.filter(state=filter_state)
    
    if filter_town:
        businesses = businesses.filter(town=filter_town)
    
    if filter_type:
        businesses = businesses.filter(type=filter_type)
    
    if filter_level:
        businesses = businesses.filter(level=filter_level)
    
    if filter_category:
        businesses = businesses.filter(category=filter_category)

    # Get distinct values for dropdowns to populate filters
    countries = Business.objects.values_list('country', flat=True).distinct()
    states = Business.objects.values_list('state', flat=True).distinct()
    towns = Business.objects.values_list('town', flat=True).distinct()
    types = Business.objects.values_list('type', flat=True).distinct()
    levels = Business.objects.values_list('level', flat=True).distinct()
    categories = Business.objects.values_list('category', flat=True).distinct()

    context = {
        'query': query,
        'filter_country': filter_country,
        'filter_state': filter_state,
        'filter_town': filter_town,
        'filter_type': filter_type,
        'filter_level': filter_level,
        'filter_category': filter_category,
        'businesses': businesses,
        'countries': countries,
        'states': states,
        'towns': towns,
        'types': types,
        'levels': levels,
        'categories': categories,
    }
    return render(request, 'business_info/business_list.html', context)


   
        
def success_page(request):
    return render(request, 'success.html')

def edit_business_view(request, id):
    business = get_object_or_404(Business, id=id)

    if request.method == 'POST':
        form = BusinessForm(request.POST, instance=business)
        if form.is_valid():
            form.save()
            return redirect('business_info:business_list')
    else:
        form = BusinessForm(instance=business)

    return render(request, 'business_info/edit_business.html', {'form': form, 'business': business})

def delete_business_view(request, id):
    business = get_object_or_404(Business, id=id)
    business.delete()
    return redirect('business_info:business_list')
