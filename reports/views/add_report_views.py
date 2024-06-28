from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from ..models import Report
from ..forms import AddReport


# Function for adding guest to database including an image upload.
def add_report_view(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """

    if request.method == "POST":
        form = AddReport(request.POST)
        if form.is_valid():
            form.save()
            report = form.save()
            report_date = report.report_date
            
            messages.add_message(
                request,
                messages.SUCCESS,
                f"Report for { report_date } has been added successfully.",
            )
            return HttpResponseRedirect("/")

    else:
        form = AddReport()

    return render(request, "reports/add_report_temp.html", {"form": form})
