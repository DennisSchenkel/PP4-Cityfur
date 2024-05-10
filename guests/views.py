from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Guest
from .models import Presence
from django.core.paginator import Paginator

# View class for guest list
def guests_list(request):
    queryset_guest = Guest.objects.all()
    queryset_presence = Presence.objects.all()
    presence = queryset_presence
    guests = queryset_guest

    context = {'presence_data': presence, 'guests_list': guests}

    return render(
        request, 
        'guests/guests_list.html', 
        context
        ) 

# View function for guest details
def guest_details(request, slug):
    queryset = Guest.objects.all()
    guest = get_object_or_404(queryset, slug=slug)

    context = {'guest': guest}

    return render(
        request,
        'guests/guest_details.html',
        context
        )
