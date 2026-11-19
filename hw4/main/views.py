from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Contact
from .forms import ContactForm


# Display all contacts and handle search
def contact_list(request):

    search = request.GET.get('search', '')

    contacts = Contact.objects.all().order_by('first_name')

    if search:
        contacts = contacts.filter(
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search)
        )

    context = {
        'contacts': contacts,
        'search': search
    }

    return render(request, 'main/contact_list.html', context)


# Add a contact
def contact_create(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('contact_list')

    else:
        form = ContactForm()

    return render(request, 'main/contact_form.html', {
        'form': form,
        'title': 'Add contact'
    })


# Edit a contact
def contact_update(request, pk):

    contact = get_object_or_404(Contact, pk=pk)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)

        if form.is_valid():
            form.save()
            return redirect('contact_list')

    else:
        form = ContactForm(instance=contact)

    return render(request, 'main/contact_form.html', {
        'form': form,
        'title': 'Edit contact'
    })


# Delete a contact
def contact_delete(request, pk):

    contact = get_object_or_404(Contact, pk=pk)

    if request.method == 'POST':
        contact.delete()

    return redirect('contact_list')