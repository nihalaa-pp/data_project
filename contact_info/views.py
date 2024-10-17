from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import Contact
from .forms import ContactForm
from django.db.models import Q
from django.urls import reverse



@login_required
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts:contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/add_contact.html', {'form': form})

@login_required
def contact_list(request):
    search_query = request.GET.get('q', '')
    selected_native_place = request.GET.get('native_place', '')
    selected_category = request.GET.get('category', '')
    selected_profession = request.GET.get('profession', '')
    selected_source = request.GET.get('source', '')
    selected_scope = request.GET.get('scope', '')
    selected_status = request.GET.get('status', '')

    contacts = Contact.objects.all()

    if search_query:
        contacts = contacts.filter(name__icontains=search_query)

    if selected_native_place:
        contacts = contacts.filter(native_place=selected_native_place)

    if selected_category:
        contacts = contacts.filter(category=selected_category)

    if selected_profession:
        contacts = contacts.filter(profession=selected_profession)

    if selected_source:
        contacts = contacts.filter(connected_source=selected_source)

    if selected_scope:
        contacts = contacts.filter(scope=selected_scope)

    if selected_status:
        contacts = contacts.filter(status=selected_status)

    # Prepare options for filters (for dropdowns)
    native_places = Contact.objects.values_list('native_place', flat=True).distinct()
    categories = Contact.objects.values_list('category', flat=True).distinct()
    professions = Contact.objects.values_list('profession', flat=True).distinct()
    sources = Contact.objects.values_list('connected_source', flat=True).distinct()
    scopes = Contact.objects.values_list('scope', flat=True).distinct()
    statuses = Contact.objects.values_list('status', flat=True).distinct()

    context = {
        'contacts': contacts,
        'search_query': search_query,
        'native_places': native_places,
        'categories': categories,
        'professions': professions,
        'sources': sources,
        'scopes': scopes,
        'statuses': statuses,
        'selected_native_place': selected_native_place,
        'selected_category': selected_category,
        'selected_profession': selected_profession,
        'selected_source': selected_source,
        'selected_scope': selected_scope,
        'selected_status': selected_status,
    }

    return render(request, 'contacts/contact_list.html', context)

@login_required
def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contacts:contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/edit_contact.html', {'form': form})

@login_required
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contacts:contact_list')
    return render(request, 'contacts/delete_contact.html', {'contact': contact})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    error_message = None  # Initialize error_message at the beginning

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Log in the user
            return redirect('contacts:landing_page')  # Redirect to landing page
        else:
            error_message = "Invalid credentials"  # Show error message if credentials are invalid

    return render(request, 'contacts/login.html', {'error_message': error_message})


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page or wherever you want




def logout_view(request):
    logout(request)
    return redirect('login') 

def landing_page(request):
    return render(request, 'contacts/landing_page.html')


