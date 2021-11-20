from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
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

# view to add employees to the database
class Employee_Create(CreateView):
    model = Employee
    fields = ['EmpNumber', 'FirstName', 'LastName', 'JobTitle', 'Username', 'Password']
    template_name = "employee_create.html"
    success_url = "/employees/"

# view to view a single employee
class Employee_Detail(DetailView):
    model = Employee
    template_name = "employee_detail.html"
    
# view to update a single employee
class Employee_Update(UpdateView):
    model = Employee
    fields = ['EmpNumber', 'FirstName', 'LastName', 'JobTitle', 'Username', 'Password']
    template_name = "employee_update.html"
    success_url = "/employees/"

# view to delete a single employee
class Employee_Delete(DeleteView):
    model = Employee
    template_name = "employee_delete.html"
    success_url = "/employees/"