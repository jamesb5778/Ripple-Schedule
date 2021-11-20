from django.urls import path
from . import views

urlpatterns = [
    # path for the home page.
    path('', views.Home.as_view(), name = "home"),
    
    # All the Paths for Employee including View All, View One, Create One, Update One, & Delete One
    #path to view all the employees
    path('employees/', views.Employees_View.as_view(), name = "employees_list"),
    #path to view only one employee
    path('employees/<int:pk>', views.Employee_Detail.as_view(), name = "employee_detail"),
    #path to create an employee 
    path('employees/new/', views.Employee_Create.as_view(), name = "employee_create"),
    #path to update an employee
    path('employees/<int:pk>/update/', views.Employee_Update.as_view(), name = "employee_update"),
    #path to delete an employee
    path('employees/<int:pk>/delete/', views.Employee_Delete.as_view(), name = "employee_delete")
]

