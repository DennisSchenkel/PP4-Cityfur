import re
from django.shortcuts import render
from ..models import Report

# View class for report list
def reports_list_all_view(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    

    
    queryset = Report.objects.order_by('-report_date')
    reports_list_all = queryset
    
    context = {'reports_list_all': reports_list_all}

    return render(
        request, 
        'reports/reports_list_all_temp.html', 
        context
        )