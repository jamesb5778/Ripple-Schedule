from django.urls import path
from . import views

urlpatterns = [
    # path for the home page.
    path('', views.Home.as_view(), name = "home"),
    # path for administrators page (Admin Only)
    path('manager_page/', views.Manager_Page.as_view(), name = "manager_page"),
    # path for the schedule Page (ALL) using a Path Coverter
    path('schedule/', views.Schedule_View.as_view(), name = "schedule_page"),
    
    # All the Paths for Employee including View All, View One, Create One, Update One, & Delete One
    #path to view all the employees
    path('employees/', views.Employees_View.as_view(), name = "employees_list"),
    #path to view only one employee
    #path to create an employee 
    #path to update an employee
    #path to delete an employee
]

