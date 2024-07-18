from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from ..models import Guest
from ..forms import AddGuest


# Function for adding guest to database including an image upload.
def add_guest_view(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """

    if request.method == "POST":
        form = AddGuest(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            guest = form.save()
            guest_name = (
                f"{guest.first_name} {guest.name_addon if guest.name_addon else ''}"
            )
            messages.add_message(
                request,
                messages.SUCCESS,
                f"Profile for { guest_name } has been added successfully.",
            )
            return HttpResponseRedirect(f"/guests/{guest.slug}")

    else:
        form = AddGuest()

    return render(request, "guests/add_guest_temp.html", {"form": form})


# Function for updating guest information
def update_guest_view(request, id):
    """_summary_

    Args:
        request (_type_): _description_
        id (_type_): _description_

    Returns:
        _type_: _description_
    """

    guest = get_object_or_404(Guest, id=id)
    guest_name = f"{guest.first_name} {guest.name_addon if guest.name_addon else ''}"
    if request.method == "POST":
        form = AddGuest(request.POST, request.FILES, instance=guest)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                f"Profile of { guest_name } has been updated successfully.",
            )
            return HttpResponseRedirect(f"/guests/{guest.slug}")

    else:
        form = AddGuest(instance=guest)

    return render(
        request, "guests/update_guest_temp.html", {"form": form, "guest": guest}
    )
