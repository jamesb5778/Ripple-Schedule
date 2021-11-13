from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
#view for the homepage
class Home(View):
    def get(self, request):
        return HttpResponse("Schedule Home Page, view schedule, make schedule, etc")

# view for the managers page
class Manager_Page(View):
    def get(self, request):
        return HttpResponse("Schedule Manager Page, view schedule, make schedule")