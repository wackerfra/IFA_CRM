from django.urls import path
from . import views

urlpatterns = [
    path('', views.operator_list, name='operator_list'),
    path('<int:pk>/', views.operator_detail, name='operator_detail'),
    path('create/', views.operator_create, name='operator_create'),
    path('<int:pk>/update/', views.operator_update, name='operator_update'),
    path('<int:pk>/delete/', views.operator_delete, name='operator_delete'),
]
