from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from ..models import Guest
from ..forms import AddGuest


# Function for adding guest to database including an image upload.
def add_guest_view(request):
    """
    This view function handles the addition of a new guest.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """

    if request.method == "POST":
        form = AddGuest(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            guest = form.save()
            guest_name = (
                f"{guest.first_name} "
                f"{guest.name_addon if guest.name_addon else ''}"
            )
            messages.add_message(
                request,
                messages.SUCCESS,
                f"Profile for {guest_name} has been added successfully.",
            )
            return HttpResponseRedirect(f"/guests/{guest.slug}")

    else:
        form = AddGuest()

    return render(request, "guests/add_guest_temp.html", {"form": form})


# Function for updating guest information
def update_guest_view(request, id):
    """
    This function helps to update the information of a guest.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the guest to be updated.

    Returns:
        HttpResponse: The HTTP response object.
    """

    guest = get_object_or_404(Guest, id=id)
    guest_name = (
        f"{guest.first_name} "
        f"{guest.name_addon if guest.name_addon else ''}"
    )
    if request.method == "POST":
        form = AddGuest(request.POST, request.FILES, instance=guest)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                f"Profile of {guest_name} has been updated successfully.",
            )
            return HttpResponseRedirect(f"/guests/{guest.slug}")

    else:
        form = AddGuest(instance=guest)

    return render(
        request, "guests/update_guest_temp.html",
        {"form": form, "guest": guest}
    )
