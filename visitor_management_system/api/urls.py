from django.urls import path
from .views import EmployeeListCreateAPIView, EmployeeRetrieveUpdateDestroyAPIView, VisitorLogListCreateAPIView, VisitorLogRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-retrieve-update-destroy'),
    path('visitor-logs/', VisitorLogListCreateAPIView.as_view(), name='visitor-log-list-create'),
    path('visitor-logs/<int:pk>/', VisitorLogRetrieveUpdateDestroyAPIView.as_view(), name='visitor-log-retrieve-update-destroy'),
]
