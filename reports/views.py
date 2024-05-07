from django.shortcuts import render
from django.views import generic
from .models import Reports
from django.core.paginator import Paginator

# View class for guest list
def reports_list(request):
    queryset = Reports.objects.all()
    paginator = Paginator(queryset, 2)  # Show 2 guests per page.

    page_number = request.GET.get('page')
    reports_list = paginator.get_page(page_number)

    context = {'reports_list': reports_list,}

    return render(
        request, 
        'reports/reports_list.html', 
        context
        )