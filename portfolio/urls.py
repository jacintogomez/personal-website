from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('education/',views.education_page,name='education'),
    path('workexperience/',views.work_experience_page,name='work experience'),
    path('projects/',views.projects_page,name='projects'),
    path('goals/',views.goals_page,name='goals'),
    path('artwork/',views.artwork_page,name='artwork'),
    path('contact',views.contact_page,name='contact'),
    path('help',views.help_page,name='help'),
]