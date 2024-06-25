from django.shortcuts import render
from datetime import datetime
from ..models import Report

# View class for report list
def reports_list_view(request):
    
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
    
    
    
    queryset = Report.objects.filter(
        report_date=date)
    reports_list = queryset
    
    context = {'reports_list': reports_list,}

    return render(
        request, 
        'reports/reports_list_temp.html', 
        context
        )