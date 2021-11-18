from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import Employee

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        LastName = self.request.GET.get("Last_Name")
        if LastName != None:
            context["employees"] = Employee.objects.filter(LastName__icontains=LastName)
            context["header"] = f"Searching For {LastName}"
        else:
            context["employees"] = Employee.objects.all()
            context["header"] = "All Employees"
        return context
    
# view for the schedule page
class Schedule_View(TemplateView):
    template_name = "schedule_page.html"
    
