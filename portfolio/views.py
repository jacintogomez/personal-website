from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request,"home.html",{})

def education_page(request):
    return render(request,"education.html",{})
def work_experience_page(request):
    return render(request,"workexperience.html",{})
def projects_page(request):
    return render(request,"projects.html",{})