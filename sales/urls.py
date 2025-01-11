from django.urls import path
from . import views

urlpatterns = [
    path('', views.sales_list, name='sales_list'),
    path('<int:pk>/', views.sales_detail, name='sales_detail'),  # Detail view URL
    path('<int:pk>/update/', views.sales_update, name='sales_update'),  # Update view
    path('<int:pk>/delete/', views.sales_delete, name='sales_delete'),  # Add delete route
    path('create/', views.sales_create, name='sales_create'),
    path('export_csv/', views.export_sales_csv, name='export_sales_csv'),
]
from django.urls import path
from . import views
