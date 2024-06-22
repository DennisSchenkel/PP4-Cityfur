from django.shortcuts import render, redirect
from datetime import datetime
from django.utils import timezone
from django.contrib import messages
from ..models import Presence, Guest
from ..forms import CheckInGuest, CheckOutGuest


# View function for guest list
def guests_list_view(request):

    # Get the selected date from the request
    selected_date = request.GET.get('date')

    #If no date is selected, default to today
    if not selected_date:
        selected_date = datetime.now().strftime('%Y-%m-%d')

    # Convert the selected date to a date object
    try:
        date = datetime.strptime(selected_date, '%Y-%m-%d').date()
    except ValueError:
        date = datetime.now().date()
    
    # Create empty lists for guests
    guests_checked_in = []
    guests_checked_out = []
    guests_not_checked_in = Guest.objects.all()
    
    # If a date is selected, get the present guests for that date
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

    # Find all guests that have a pickup scheduled
    presences = {presence.guest.id: presence for presence in Presence.objects.filter(date=date)}

    # Create forms for check-in and check-out guests
    check_in = CheckInGuest()
    check_out = CheckOutGuest()

    # Handle POST requests
    if request.method == 'POST':
        
        # Get the selected date from the POST request
        selected_date = request.POST.get('date', selected_date)
        try:
            date = datetime.strptime(selected_date, '%Y-%m-%d').date()
        except ValueError:
            date = datetime.now().date()
        
        
        # Check-In
        # If the check-in button is clicked, create a form for checking in guests
        if 'checkin' in request.POST:
            check_in = CheckInGuest(request.POST)
            if check_in.is_valid():
                guest = check_in.cleaned_data['guest']
                guest_name = f"{guest.first_name} {guest.name_addon if guest.name_addon else ''}"
                checkin_time = timezone.now().time()

                # Check if the guest is already checked at the selected date
                presence, created = Presence.objects.get_or_create(
                    guest=guest,
                    date=date,
                    defaults={'check_in': checkin_time}
                )

                # If the guest is not checked in at the selected date, check them in
                if created:
                    messages.add_message(
                        request, messages.SUCCESS,
                        f'Check-In for {guest_name} was successful.'
                    )
                elif presence.check_in is None:
                    presence.check_in = checkin_time
                    presence.save()
                    messages.add_message(
                        request, messages.SUCCESS,
                        f'Check-In for {guest_name} was successful.'
                    )
                else:
                    messages.add_message(
                        request, messages.ERROR,
                        'Check-In failed: {guest_name} is already checked in or presence already exists.'
                    )

                return redirect(f"{request.path}?date={selected_date}")
            else:
                messages.add_message(
                    request, messages.ERROR,
                    'Check-In form is not valid.'
                )


        # Check-Out
        # If the check-out button is clicked, create a form for checking out guests
        elif 'checkout' in request.POST:
            check_out = CheckOutGuest(request.POST)
            if check_out.is_valid():
                guest = check_out.cleaned_data['guest']
                guest_name = f"{guest.first_name} {guest.name_addon if guest.name_addon else ''}"
                checkout_time = timezone.now().time()

                # Check if the guest is already checked out at the selected date
                presence = Presence.objects.filter(
                    guest=guest,
                    date=date
                ).first()
                            
                # If the guest is checked in at the selected date, check them out
                if presence:
                    if presence.check_in is not None and presence.check_out is None:
                        presence.check_out = checkout_time
                        presence.save()
                        messages.add_message(
                            request, messages.SUCCESS,
                            f'Check-Out for {guest_name} was successful.'
                        )
                    else:
                        messages.add_message(
                            request, messages.ERROR,
                            f'Check-Out failed: {guest_name} is not checked in or already checked out.'
                        )
                else:
                    messages.add_message(
                        request, messages.ERROR,
                        f'Check-Out failed: presence for {guest_name}record does not exist.'
                    )

                return redirect(f"{request.path}?date={selected_date}")
            else:
                messages.add_message(
                    request, messages.ERROR,
                    'Check-Out form is not valid.'
                )
        
        
        # Undo Check-In
        # If the undo check-in button is clicked, delete the presence to undo the check-in
        elif 'undo_checkin' in request.POST:
            guest_id = request.POST.get('guest')
            presence = Presence.objects.filter(guest_id=guest_id, date=date).first()
            if presence and presence.check_in is not None:
                guest = presence.guest
                guest_name = f"{guest.first_name} {guest.name_addon if guest.name_addon else ''}"  
                presence.delete()
                messages.add_message(
                    request, messages.SUCCESS,
                    f'Check-In for {guest_name} was undone successfully.'
                )
            else:
                messages.add_message(
                    request, messages.ERROR,
                    f'Undo Check-In failed: no check-in record found for {guest_name}.'
                )

            return redirect(f"{request.path}?date={selected_date}")


        # Undo Check-Out
        # If the undo check-out button is clicked, set the check-out time to None
        elif 'undo_checkout' in request.POST:
            guest_id = request.POST.get('guest')

            # Find the presence for the guest at the selected date
            presence = Presence.objects.filter(guest_id=guest_id, date=date).first()
            
            
            
            # If the guest is checked out, set the check-out time to None to undo the check-out
            if presence and presence.check_out is not None:
                guest = presence.guest
                guest_name = f"{guest.first_name} {guest.name_addon if guest.name_addon else ''}"              
                presence.check_out = None
                presence.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    f'Check-Out for {guest_name} was undone successfully.'
                )
            else:
                messages.add_message(
                    request, messages.ERROR,
                    f'Undo Check-Out failed: no check-out record found for {guest_name}.'
                )

            return redirect(f"{request.path}?date={selected_date}")
    
    
    # Get the total number of guests checked in and checked out today    
    todays_guest_count = len(guests_checked_in) + len(guests_checked_out)



    context = {
        'guests_checked_in': guests_checked_in,
        'guests_checked_out': guests_checked_out,
        'guests_not_checked_in': guests_not_checked_in,
        'presences': presences,
        'selected_date': selected_date,
        'check_in_form': check_in,
        'check_out_form': check_out,
        'todays_guest_count': todays_guest_count
        }
    
    return render(
        request, 
        './guests/guests_list_temp.html', 
        context
    )
