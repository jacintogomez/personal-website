from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('about/',views.about_page,name='about'),
    path('education/',views.education_page,name='education'),
    path('work_experience/',views.work_experience_page,name='work_experience'),
    path('projects/',views.projects_page,name='projects'),
    path('software/',views.software_projects_page,name='software'),
    path('palloc/',views.palloc_page,name='palloc'),
    path('d3clarity/',views.d3clarity,name='d3clarity'),
    path('d3color/',views.d3color,name='d3color'),
    path('d3aiddata/',views.d3aiddata,name='d3aiddata'),
    path('d3hatecrimes/',views.d3hatecrimes,name='d3hatecrimes'),
    path('mechanical/',views.mechanical_projects_page,name='mechanical'),
    path('goals/',views.goals_page,name='goals'),
    path('artwork/',views.artwork_page,name='artwork'),
    path('contact',views.contact_page,name='contact'),
    path('help',views.help_page,name='help'),
]