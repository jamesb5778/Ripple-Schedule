from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
#view for the homepage
class Home(TemplateView):
    template_name="home.html"
    
# view for the managers page
class Manager_Page(View):
    def get(self, request):
        return HttpResponse("Schedule Manager Page, view schedule, make schedule")