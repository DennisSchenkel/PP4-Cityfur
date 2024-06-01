from django.shortcuts import render
from ..models import Guest, Presence
from datetime import datetime

# View function for guest list
def guests_list(request):
    # Get the selected date from the request
    selected_date = request.GET.get('date')
    
    #If no date is selected, default to today
    if not selected_date:
        selected_date = datetime.now().strftime('%Y-%m-%d')

    
    guests_checked_in = []
    guests_checked_out = []
    
    # If a date is selected, get the guests for that date
    if selected_date:
        try:
            # Convert the selected date to a date object
            date = datetime.strptime(selected_date, '%Y-%m-%d').date()
            
            # Find all presences for the selected date
            presences_checked_in = Presence.objects.filter(date=date, check_in__isnull=False, check_out__isnull=True).select_related('guest')
            # Extract the guests from the presences
            guests_checked_in = [presence.guest for presence in presences_checked_in]
            
            # Find all presences for the selected date where guests have checked out
            presences_checked_out = Presence.objects.filter(date=date, check_out__isnull=False).select_related('guest')
            # Extract the guests from the presences
            guests_checked_out = [presence.guest for presence in presences_checked_out]
            
        except ValueError:
            guests_checked_in = []
            guests_checked_out = []
    else:
        guests_checked_in = []
        guests_checked_out = []

    context = {
        'guests_checked_in': guests_checked_in,
        'guests_checked_out': guests_checked_out,
        'selected_date': selected_date
        }
    
    return render(
        request, 
        './guests/guests_list.html', 
        context
    )

