from django.shortcuts import render, redirect
from ..models import Presence, Guest
from ..forms import CheckInGuest, CheckOutGuest
from datetime import datetime
from django.utils import timezone

# View function for guest list
def guests_list(request):
    # Get the selected date from the request
    selected_date = request.GET.get('date')
    
    #If no date is selected, default to today
    if not selected_date:
        selected_date = datetime.now().strftime('%Y-%m-%d')

    guests_checked_in = []
    guests_checked_out = []
    guests_not_checked_in = Guest.objects.all()
    
    # Convert the selected date to a date object
    try:
        date = datetime.strptime(selected_date, '%Y-%m-%d').date()
    except ValueError:
        date = datetime.now().date()
    
    # If a date is selected, get the guests for that date
    # Find all presences for the selected date
    presences_checked_in = Presence.objects.filter(date=date, check_in__isnull=False, check_out__isnull=True).select_related('guest')
    # Extract the guests from the presences
    guests_checked_in = [presence.guest for presence in presences_checked_in]
    
    # Find all presences for the selected date where guests have checked out
    presences_checked_out = Presence.objects.filter(date=date, check_out__isnull=False).select_related('guest')
    # Extract the guests from the presences
    guests_checked_out = [presence.guest for presence in presences_checked_out]
    
    # Find all guests that are not checked in
    # Exclude guests that are already checked in
    guests_not_checked_in = guests_not_checked_in.exclude(id__in=[guest.id for guest in guests_checked_in])
    # Exclude guests that are already checked out
    guests_not_checked_in = guests_not_checked_in.exclude(id__in=[guest.id for guest in guests_checked_out])


    check_in = CheckInGuest()
    check_out = CheckOutGuest()

    if request.method == 'POST':
        
        selected_date = request.POST.get('date', selected_date)
        try:
            date = datetime.strptime(selected_date, '%Y-%m-%d').date()
        except ValueError:
            date = datetime.now().date()
        
        # Check-In
        if 'checkin' in request.POST:
            check_in = CheckInGuest(request.POST)
            if check_in.is_valid():
                guest = check_in.cleaned_data['guest']
                checkin_time = timezone.now().time()

                # Check if the guest is already checked at the selected date
                presence, created = Presence.objects.get_or_create(
                    guest=guest,
                    date=date,
                    defaults={'check_in': checkin_time}
                )

                # If the guest is not checked at the selected date, check them in
                if not created and presence.check_in is None:
                    presence.check_in = checkin_time
                    presence.save()

                return redirect(f"{request.path}?date={selected_date}")

        # Check-Out
        elif 'checkout' in request.POST:
            check_out = CheckOutGuest(request.POST)
            if check_out.is_valid():
                guest = check_out.cleaned_data['guest']
                checkout_time = timezone.now().time()

                # Check if the guest is already checked out at the selected date
                presence = Presence.objects.filter(
                    guest=guest,
                    date=date
                ).first()
                            
                # If the guest is checked in at the selected date, check them out
                if presence and presence.check_out is None:
                    presence.check_out = checkout_time
                    presence.save()

                return redirect(f"{request.path}?date={selected_date}")

        
        # Undo Check-In
        elif 'undo_checkin' in request.POST:
            guest_id = request.POST.get('guest')

            Presence.objects.filter(guest_id=guest_id, date=date).delete()
                
            return redirect(f"{request.path}?date={selected_date}")

        # Undo Check-Out
        elif 'undo_checkout' in request.POST:
            guest_id = request.POST.get('guest')

            presence = Presence.objects.filter(guest_id=guest_id, date=date).first()
            if presence and presence.check_out is not None:
                presence.check_out = None
                presence.save()

                return redirect(f"{request.path}?date={selected_date}")
        
    todays_guest_count = len(guests_checked_in) + len(guests_checked_out)

    context = {
        'guests_checked_in': guests_checked_in,
        'guests_checked_out': guests_checked_out,
        'guests_not_checked_in': guests_not_checked_in,
        'selected_date': selected_date,
        'check_in_form': check_in,
        'check_out_form': check_out,
        'todays_guest_count': todays_guest_count
        }
    
    return render(
        request, 
        './guests/guests_list.html', 
        context
    )
