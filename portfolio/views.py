from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request,"home.html",{})

def education_page(request):
    return render(request,"education.html",{})
def about_page(request):
    return render(request,"about.html",{})
def work_experience_page(request):
    return render(request,"workexperience.html",{})
def projects_page(request):
    return render(request,"projects.html",{})

def software_projects_page(request):
    return render(request,"software.html",{})
def algos_page(request):
    return render(request,"algoconsole.html",{})
def palloc_page(request):
    return render(request,"payalloc.html",{})
def d3clarity(request):
    return render(request,"d3clarity.html",{})
def d3color(request):
    return render(request,"d3color.html",{})
def d3hatecrimes(request):
    return render(request,"d3hatecrimes.html",{})
def d3aiddata(request):
    return render(request,"d3aiddata.html",{})
def mechanical_projects_page(request):
    return render(request,"mechanical.html",{})
def goals_page(request):
    return render(request,"goals.html",{})
def artwork_page(request):
    return render(request,"artwork.html",{})
def contact_page(request):
    return render(request,"contact.html",{})
def help_page(request):
    return render(request,"help.html",{})