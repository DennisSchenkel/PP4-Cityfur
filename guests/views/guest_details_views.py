from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from ..models import Guest
from reports.models import Report


# View function for guest details
def guest_details_view(request, slug):
    """_summary_

    Args:
        request (_type_): _description_
        slug (_type_): _description_

    Returns:
        _type_: _description_
    """

    queryset = Guest.objects.all()
    guest = get_object_or_404(queryset, slug=slug)

    def guest_custumor():
        if guest.customer_id:
            return guest.customer_id
        else:
            return None

    customer = guest_custumor()

    if request.method == "POST" and "delete" in request.POST:
        guest_name = (
            f"{guest.first_name} "
            f"{guest.name_addon if guest.name_addon else ''}"
        )
        guest.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            f"Profile of {guest_name} has been deleted successfully.",
        )
        return redirect("/")

    guest_reports = (
        Report.objects.filter(guests=guest).order_by('-report_date')
    )
    context = {"guest": guest,
               "customer": customer,
               "guest_reports": guest_reports,
               }

    return render(request, "./guests/guest_details_temp.html", context)
