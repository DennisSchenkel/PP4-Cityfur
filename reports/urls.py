from .views.reports_list_views import reports_list_view
from .views.add_report_views import add_report_view
from django.urls import path

urlpatterns = [
    path('', reports_list_view, name='home'),
    path('reports/', reports_list_view, name='reports_list_temp'),
    path('reports/add_report/', add_report_view, name='add_report_temp'),
]