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
            'house_name': request.POST.get('house_name'),  # Retaining this line from the second change
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

def business_list(request):
    query = request.GET.get('q', '')
    filter_town = request.GET.get('town', '')
    filter_state = request.GET.get('state', '')
    filter_country = request.GET.get('country', '')
    filter_type = request.GET.get('type', '')  # Retaining this line from the second change
    
    businesses = Business.objects.all()

    # Search functionality
    if query:
        businesses = businesses.filter(
            Q(name_of_firm__icontains=query) |
            Q(town__icontains=query) |
            Q(website_url__icontains=query)
        )

    # Filtering functionality
    if filter_town:
        businesses = businesses.filter(town__icontains=filter_town)
    if filter_state:
        businesses = businesses.filter(state__icontains=filter_state)
    if filter_country:
        businesses = businesses.filter(country__icontains=filter_country)
    if filter_type:
        businesses = businesses.filter(type__icontains=filter_type)  # Retaining this line from the second change

    # Get distinct values for filters
    towns = Business.objects.values_list('town', flat=True).distinct()
    states = Business.objects.values_list('state', flat=True).distinct()
    countries = Business.objects.values_list('country', flat=True).distinct()
    types = Business.objects.values_list('type', flat=True).distinct()  # Retaining this line from the second change

    return render(request, 'business_info/business_list.html', {
        'businesses': businesses,
        'query': query,
        'filter_town': filter_town,
        'filter_state': filter_state,
        'filter_country': filter_country,
        'filter_type': filter_type,  # Retaining this line from the second change
        'towns': towns,
        'states': states,
        'countries': countries,
        'types': types  # Retaining this line from the second change
    })

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
