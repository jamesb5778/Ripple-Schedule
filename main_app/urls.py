from django.urls import path
from . import views

urlpatterns = [
    # path for the login page
    # path for the home page.
    path('', views.Home.as_view(), name = "home"),
    # path for the schedule Page (ALL)
    # path for administrators page (Admin Only)
    path('manager_page/', views.Manager_Page.as_view(), name = "manager_page")
    # path for create, update, delete and post(submit) a schedule (Admin Only)
    
]

