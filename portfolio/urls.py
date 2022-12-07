from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('education/',views.education_page,name='education'),
    path('work_experience/',views.work_experience_page,name='work_experience'),
    path('projects/',views.projects_page,name='projects'),
    path('software/',views.software_projects_page,name='software'),
    path('d3clarity/',views.d3clarity,name='d3clarity'),
    path('mechanical/',views.mechanical_projects_page,name='mechanical'),
    path('goals/',views.goals_page,name='goals'),
    path('artwork/',views.artwork_page,name='artwork'),
    path('contact',views.contact_page,name='contact'),
    path('help',views.help_page,name='help'),
]