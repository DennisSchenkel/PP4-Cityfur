from calendar import c
from django.shortcuts import render, get_object_or_404
from ..models import Guest

# View function for guest details
def guest_details_view(request, slug):
    queryset = Guest.objects.all()
    guest = get_object_or_404(queryset, slug=slug)
    
    
    def guest_custumor():
        if guest.customer_id:
            return guest.customer_id
        else:
            return None
    
    customer = guest_custumor()

    context = {'guest': guest, customer: customer}

    return render(
        request,
        './guests/guest_details_temp.html',
        context
        )

