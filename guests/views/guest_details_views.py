from django.shortcuts import render, get_object_or_404
from ..models import Guest

# View function for guest details
def guest_details(request, slug):
    queryset = Guest.objects.all()
    guest = get_object_or_404(queryset, slug=slug)

    context = {'guest': guest}

    return render(
        request,
        './guests/guest_details.html',
        context
        )

