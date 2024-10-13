# service/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_service_request, name='create_request'),
    path('status/<int:request_id>/', views.request_status, name='request_status'),
    path('notifications/', views.notifications, name='notifications'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
