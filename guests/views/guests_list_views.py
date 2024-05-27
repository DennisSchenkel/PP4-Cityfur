from django.shortcuts import render
from ..models import Guest, Presence
from datetime import datetime

# View function for guest list
def guests_list(request):
    selected_date = request.GET.get('date')
    
    if not selected_date:
        selected_date = datetime.now().strftime('%Y-%m-%d')

    
    guests = []

    if selected_date:
        try:
            date_obj = datetime.strptime(selected_date, '%Y-%m-%d').date()
            # Find all presences for the selected date
            presences = Presence.objects.filter(date=date_obj).select_related('guest')
            # Extract the guests from the presences
            guests = [presence.guest for presence in presences]
        except ValueError:
            guests = []
    else:
        guests = []

    context = {'guests_list': guests, 'selected_date': selected_date}
    
    return render(
        request, 
        './guests/guests_list.html', 
        context
    )

