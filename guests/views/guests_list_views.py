from django.shortcuts import render
from ..models import Guest
from ..models import Presence

# View class for guest list
def guests_list(request):
    queryset_guest = Guest.objects.all()
    queryset_presence = Presence.objects.all()
    presence = queryset_presence
    guests = queryset_guest

    context = {'presence_data': presence, 'guests_list': guests}

    return render(
        request, 
        './guests/guests_list.html', 
        context
        ) 
