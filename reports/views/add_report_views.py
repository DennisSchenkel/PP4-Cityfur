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
            return HttpResponseRedirect(f"/reports/?date={report_date}")

    else:
        form = AddReport()

    return render(request, "reports/add_report_temp.html", {"form": form})


# Function for updating report
def update_report_view(request, id):
    """_summary_

    Args:
        request (_type_): _description_
        id (_type_): _description_

    Returns:
        _type_: _description_
    """

    report = get_object_or_404(Report, id=id)
    report_date = report.report_date
    if request.method == "POST":
        form = AddReport(request.POST, request.FILES, instance=report)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                f"Report for {report_date} has been updated successfully.",
            )
            return HttpResponseRedirect(f"/reports/?date={report_date}")

    else:
        form = AddReport(instance=report)

    return render(request, "reports/update_report_temp.html", {"form": form, "report": report})
