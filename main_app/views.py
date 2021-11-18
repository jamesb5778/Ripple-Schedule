from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
#view for the homepage
class Home(TemplateView):
    template_name = "home.html"
    
# view for the managers page
class Manager_Page(TemplateView):
    template_name = "manager_page.html"

# view to see all the employees
class Employees_View(TemplateView):
    template_name = "employees_view.html"
    
# view for the schedule page
class Schedule_View(TemplateView):
    template_name = "schedule_page.html"
    
