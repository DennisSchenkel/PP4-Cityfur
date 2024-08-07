from django.shortcuts import render
from datetime import datetime
from ..models import Report


# View function for report list
def reports_list_view(request):
    """
    Render the report list for a selected date.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered response.
    """

    # Get the selected date from the request
    selected_date = request.GET.get("date")

    # If no date is selected, default to today
    if not selected_date:
        selected_date = datetime.now().strftime("%Y-%m-%d")

    # Convert the selected date to a date object
    try:
        date = datetime.strptime(selected_date, "%Y-%m-%d").date()
    except ValueError:
        date = datetime.now().date()

    queryset = Report.objects.filter(report_date=date)
    reports_list = queryset

    context = {'reports_list': reports_list}

    return render(
        request,
        'reports/reports_list_temp.html',
        context
        )


# View function for report list
def reports_list_all_view(request):
    """
    Render the list of all reports.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered response.
    """

    queryset = Report.objects.order_by('-report_date')
    reports_list_all = queryset

    context = {'reports_list_all': reports_list_all}

    return render(
        request,
        'reports/reports_list_all_temp.html',
        context
        )
