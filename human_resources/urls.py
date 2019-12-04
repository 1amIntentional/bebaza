from django.urls import path

from . import views

app_name = 'human_resources'
urlpatterns = [
    # ex: /human-resources/create-employee
    path('create-employee/', views.CreateEmployeeView.as_view(), name='create-employee'),
    path('employee/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
]
