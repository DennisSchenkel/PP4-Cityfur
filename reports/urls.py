from django.urls import path
from .views.reports_list_views import reports_list_view, reports_list_all_view
from .views.add_report_views import update_report_view, add_report_view
from .views.report_details_views import report_details_view

urlpatterns = [
    path('', reports_list_view, name='home'),
    path('reports/', reports_list_view, name='reports_list_temp'),
    path('reports/all/', reports_list_all_view, name='reports_list_all_temp'),
    path('reports/add_report/', add_report_view, name='add_report_temp'),
    path(
        'reports/update_report/<int:id>/',
        update_report_view, name='update_report_temp'
        ),
    path(
        'reports/report_details/<int:id>/',
        report_details_view, name='report_details_temp'
        ),
]
