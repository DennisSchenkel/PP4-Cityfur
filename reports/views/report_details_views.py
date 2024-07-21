
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..models import Report


def report_details_view(request, id):
    """
    Render the report details view.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the report.

    Returns:
        HttpResponse: The rendered report details view.
    """

    report = get_object_or_404(Report, id=id)

    if request.method == 'POST':
        report_date = report.report_date.strftime('%Y-%m-%d')
        report.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            f"Report for {report_date} "
            f"was deleted successfully.",
            )
        return redirect(f'/reports/?date={report_date}')

    context = {
        'report': report,
    }
    return render(request, 'reports/report_details_temp.html', context)
