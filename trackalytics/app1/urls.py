# trackalytics/app1/urls.py
from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('inventory/', views.inventory, name='inventory'),
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('history/', views.inventory_history, name='inventory_history'),
    path('reports/', views.reports_exports, name='reports_exports'),
    path('report/generate/', views.generate_inventory_report, name='generate_inventory_report'),
    path('export/', views.export_data, name='export_data'),
    path('report/download/<int:report_id>/', views.download_report, name='download_report'),
    path('report/delete/<int:report_id>/', views.delete_report, name='delete_report'),
    path('activity/', views.activity_log, name='activity_log'),
    path('register/', views.register, name='register'),
    path('api/activity-logs/', views.api_activity_logs, name='api_activity_logs'),
]