from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Guest
from django.core.paginator import Paginator

# View class for guest list
def guests_list(request):
    queryset = Guest.objects.all()
    paginator = Paginator(queryset, 2)  # Show 2 guests per page.

    page_number = request.GET.get('page')
    guests_list = paginator.get_page(page_number)

    context = {'guests_list': guests_list,}

    return render(
        request, 
        'guests/guests_list.html', 
        context
        )
    

# View function for guest details
def guest_details(request, slug):
    queryset = Guest.objects.all()
    guest = get_object_or_404(queryset, slug=slug)

    context = {'guest': guest,}

    return render(
        request,
        'guests/guest_details.html',
        context
    )