from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_list, name='report_list'),
    path('<int:pk>/', views.report_detail, name='report_detail'),  # Detail view
    path('<int:pk>/update/', views.report_update, name='report_update'),  # Update view
    path('<int:pk>/delete/', views.report_delete, name='report_delete'),  # Delete view
    path('export/csv/', views.report_export_csv, name='report_export_csv'),  # CSV Export
    path('export/pdf/', views.report_export_pdf, name='report_export_pdf'),  # PDF Export
    path('create/', views.report_create, name='report_create'),  # Add route for creating a new report
]